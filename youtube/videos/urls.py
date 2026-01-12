from django.urls import path
from . import views

app_name = "videos"

urlpatterns = [
    path("", views.video_list, name="list"),
    path("trending/", views.video_trending, name="trending"),
    path("upload/", views.video_upload_page, name="upload"),
    path("upload/submit/", views.video_upload, name="upload_submit"),
    path("<int:video_id>", views.video_detail, name="detail"),
    path("channel/<str:username>/", views.channel_videos, name="channel"),
    path("<int:video_id>/delete/", views.delete_video, name="delete"),
    path("<int:video_id>/vote/", views.video_vote, name="vote")
]