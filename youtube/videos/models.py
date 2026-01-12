from django.db import models
from django.contrib.auth.models import User
from .imagekit_client import (
    get_optimized_video_url, get_streaming_url, get_thumbnail_url, add_image_watermark
)


class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="videos")
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)

    file_id = models.CharField(max_length=200, blank=True, null=True)
    video_url = models.URLField(max_length=500, blank=True, null=True)
    thumbnail_url = models.URLField(max_length=500, blank=True)

    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    # YouTube Support
    youtube_id = models.CharField(max_length=20, blank=True, help_text="Optional: YouTube Video ID for external videos")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    @property
    def is_youtube(self):
        return bool(self.youtube_id)

    @property
    def display_thumbnail_url(self):
        if self.is_youtube:
            return f"https://img.youtube.com/vi/{self.youtube_id}/maxresdefault.jpg"
        if self.thumbnail_url and "/thumbnails/" in self.thumbnail_url:
            return add_image_watermark(self.thumbnail_url, self.user.username)
        return self.generated_thumbnail_url

    @property
    def generated_thumbnail_url(self):
        if not self.video_url:
            return ""
        return get_thumbnail_url(self.video_url, self.user.username)

    @property
    def streaming_url(self):
        if not self.video_url:
            return ""
        return get_streaming_url(self.video_url)

    @property
    def optimized_url(self):
        if not self.video_url:
            return ""
        return get_optimized_video_url(self.video_url)


class VideoLike(models.Model):
    LIKE = 1
    DISLIKE = -1
    LIKE_CHOICES = [
        (LIKE, "Like"),
        (DISLIKE, "Dislike")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="user_likes")
    value = models.SmallIntegerField(choices=LIKE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["user", "video"]

    def __str__(self):
        action = "liked" if self.value == self.LIKE else "disliked"
        return f"{self.user.username} {action} {self.video.title}"