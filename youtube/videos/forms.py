from django import forms


class VideoUploadForm(forms.Form):

    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Enter video title"
            }
        )
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-input",
                "placeholder": "Enter video description",
                "rows": 4
            }
        )
    )
    video_file = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={
            "class": "form-input",
            "accept": "video/*"
        })
    )

    youtube_id = forms.CharField(
        required=False,
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Enter YouTube Video ID (e.g. dQw4w9WgXcQ)"
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        video_file = cleaned_data.get("video_file")
        youtube_id = cleaned_data.get("youtube_id")

        if not video_file and not youtube_id:
            raise forms.ValidationError("You must provide either a video file or a YouTube Video ID.")
        
        return cleaned_data

    def clean_video_file(self):
        video = self.cleaned_data.get("video_file")
        if video:
            if video.size > 100 * 1024 * 1024:
                raise forms.ValidationError("Video must be under 100mb")

            allowed_types = ["video/mp4", "video/webm", "video/quicktime", "video/x-msvideo"]
            if video.content_type not in allowed_types:
                raise forms.ValidationError("This video type is not allowed.")

        return video
