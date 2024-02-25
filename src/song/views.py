from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from song.models import Song, Artist
from django_filters.rest_framework import DjangoFilterBackend
from song.serializers import SongSerializer, SongSearchSerializer, ArtistSerializer
from song.pagination import CustomPagination
from song.filters import SongFilter


class SongListAPIView(ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SongFilter


class SongSearchAPIView(APIView):
    @swagger_auto_schema(
        query_serializer=SongSearchSerializer(),
        responses={200: SongSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):

        LIMIT_ITEMS = 20

        search_text = request.query_params.get("search_text", None)

        if search_text is not None:
            title_matches = Song.objects.filter(title__icontains=search_text).order_by(
                "title"
            )[:LIMIT_ITEMS]
            artist_matches = Artist.objects.filter(
                name__icontains=search_text
            ).order_by("name")[:LIMIT_ITEMS]
        else:
            title_matches = Song.objects.none()
            artist_matches = Artist.objects.none()

        title_serializer = SongSerializer(
            title_matches, many=True, context={"request": request}
        )
        artist_serializer = ArtistSerializer(
            artist_matches, many=True, context={"request": request}
        )

        combined_data = {
            "title_matches": title_serializer.data,
            "artist_matches": artist_serializer.data,
        }

        return Response(combined_data)


class SongHomeAPIView(APIView):
    def get(self, request, *args, **kwargs):

        LIMIT_ITEMS = 10

        new_songs = Song.objects.all().order_by("-created_at")[:LIMIT_ITEMS]
        top_songs = Song.objects.all()[:LIMIT_ITEMS]

        new_songs_serializer = SongSerializer(
            new_songs, many=True, context={"request": request}
        )
        top_songs_serializer = SongSerializer(
            top_songs, many=True, context={"request": request}
        )

        combined_data = {
            "new_songs": new_songs_serializer.data,
            "top_songs": top_songs_serializer.data,
        }

        return Response(combined_data)
