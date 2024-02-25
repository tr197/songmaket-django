from uuid import uuid4 as generate_id
from django.db import models
from user.models import User
from song.services.validator import validate_audio_file


class Artist(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_id, editable=False)
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


class Album(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_id, editable=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField()

    def __str__(self):
        return self.title


class Song(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_id, editable=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, blank=True)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True, blank=True)
    audio = models.FileField(
        upload_to="songs/audio/",
        null=False,
        blank=False,
        help_text="Upload a song file (mp3)",
        validators=[validate_audio_file],
    )
    image = models.ImageField(null=True, blank=False, upload_to="songs/image/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "song"

    def __str__(self):
        return self.title


class Playlist(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_id, editable=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.title
