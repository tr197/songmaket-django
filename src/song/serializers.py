from rest_framework import serializers
from song.models import Song, Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"


class SongSerializer(serializers.ModelSerializer):

    artist_name = serializers.CharField(source="artist.name", read_only=True)

    class Meta:
        model = Song
        fields = [
            "id",
            "title",
            "artist_name",
            "album",
            "audio",
            "image",
            "created_at",
        ]


class SongSearchSerializer(serializers.Serializer):
    search_text = serializers.CharField(
        max_length=100,
        required=False,
        help_text="Text to search for in song titles and artist names.",
    )
