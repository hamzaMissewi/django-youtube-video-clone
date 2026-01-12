from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import Video, VideoLike
from .forms import VideoUploadForm
from .imagekit_client import upload_video, upload_thumbnail, delete_video


def video_detail(request, video_id):
    video = get_object_or_404(Video.objects, id=video_id)

    video.views += 1
    video.save(update_fields=["views"])

    user_vote = None
    if request.user.is_authenticated:
        like = VideoLike.objects.filter(user=request.user, video=video).first()
        if like:
            user_vote = like.value

    return render(request, "videos/detail.html", {"video": video, "user_vote": user_vote})


def video_list(request):
    query = request.GET.get("q")
    if query:
        videos = Video.objects.filter(
            models.Q(title__icontains=query) | 
            models.Q(description__icontains=query)
        ).distinct()
    else:
        videos = Video.objects.all()
    
    return render(request, 'videos/list.html', {"videos": videos, "query": query})


def video_trending(request):
    videos = Video.objects.all().order_by("-views")[:20]
    return render(request, 'videos/list.html', {"videos": videos, "is_trending": True})


def channel_videos(request, username):
    videos = Video.objects.filter(user__username=username)
    return render(request, "videos/channel.html", {"videos": videos, "channel_name": username})


@login_required
@require_POST
def video_upload(request):
    form = VideoUploadForm(request.POST, request.FILES)
    if form.is_valid():
        video_file = form.cleaned_data.get('video_file')
        youtube_id = form.cleaned_data.get('youtube_id')
        custom_thumbnail = request.POST.get("thumbnail_data", "")

        try:
            file_id = ""
            video_url = ""
            
            if video_file:
                result = upload_video(
                    file_data=video_file.read(),
                    file_name=video_file.name
                )
                file_id = result["file_id"]
                video_url = result["url"]

            thumbnail_url = ""
            if custom_thumbnail and custom_thumbnail.startswith("data:image"):
                try:
                    base_name = video_file.name.rsplit(".", 1)[0] if video_file else f"yt_{youtube_id}"
                    thumb_result = upload_thumbnail(
                        file_data=custom_thumbnail,
                        file_name=base_name + "_thumb.jpg"
                    )
                    thumbnail_url = thumb_result["url"]
                except Exception as e:
                    print(e)
                    pass

            video = Video.objects.create(
                user=request.user,
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                file_id=file_id,
                video_url=video_url,
                youtube_id=youtube_id,
                thumbnail_url=thumbnail_url,
            )

            return JsonResponse({
                "success": True,
                "video_id": video.id,
                "message": "Video uploaded successfully"
            })
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    errors = []
    for field, field_errors in form.errors.items():
        for error in field_errors:
            errors.append(f"{field}: {error}" if field != "__all__" else error)
    return JsonResponse({"success": False, "error": "; ".join(errors)})


@login_required
def video_upload_page(request):
    return render(request, "videos/upload.html", {"form": VideoUploadForm()})


@login_required
@require_POST
def delete_video(request, video_id):
    video = get_object_or_404(Video, id=video_id, user=request.user)

    try:
        delete_video(video.file_id)
    except Exception as e:
        print(e)
        pass

    video.delete()

    return JsonResponse({"success": True, "message": "video deleted"})


@login_required
@require_POST
def video_vote(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    vote_type = request.POST.get("vote")

    if vote_type not in ["like", "dislike"]:
        return JsonResponse({"success": False, "error": "Invalid vote"}, status=400)

    value = VideoLike.LIKE if vote_type == "like" else VideoLike.DISLIKE

    existing_vote = VideoLike.objects.filter(user=request.user, video=video).first()

    if existing_vote:
        if existing_vote.value == value:
            if value == VideoLike.LIKE:
                video.likes -= 1
            else:
                video.dislikes -= 1
            existing_vote.delete()
            user_vote = None
        else:
            if value == VideoLike.LIKE:
                video.likes += 1
                video.dislikes -= 1
            else:
                video.likes -=1
                video.dislikes += 1
            existing_vote.value = value
            existing_vote.save()
            user_vote = value
    else:
        VideoLike.objects.create(user=request.user, video=video, value=value)
        if value == VideoLike.LIKE:
            video.likes += 1
        else:
            video.dislikes += 1
        user_vote = value

    video.save(update_fields=["likes", "dislikes"])

    return JsonResponse({
        "likes": video.likes,
        "dislikes": video.dislikes,
        "user_vote": user_vote
    })