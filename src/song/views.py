from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from song.models import Song, Artist
from django_filters.rest_framework import DjangoFilterBackend
from song.serializers import (
    SongSerializer,
    SongSearchSerializer,
    ArtistSerializer,
    IncreaseViewSerializer,
)
from song.pagination import CustomPagination, PAGE_SIZE
from song.filters import SongFilter
from asset.models import Banner
from asset.serializers import BannerSerializer


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
            songs_matches = Song.objects.filter(title__icontains=search_text).order_by(
                "title"
            )[:LIMIT_ITEMS]
            artists_matches = Artist.objects.filter(
                name__icontains=search_text
            ).order_by("name")[:LIMIT_ITEMS]
        else:
            songs_matches = Song.objects.none()
            artists_matches = Artist.objects.none()

        song_serializer = SongSerializer(
            songs_matches, many=True, context={"request": request}
        )
        artist_serializer = ArtistSerializer(
            artists_matches, many=True, context={"request": request}
        )

        combined_data = {
            "songs_matches": song_serializer.data,
            "artists_matches": artist_serializer.data,
        }

        return Response(combined_data)


class SongHomeAPIView(APIView):
    def get(self, request, *args, **kwargs):

        total = Song.objects.count()
        new_songs = Song.objects.order_by("-created_at")[:PAGE_SIZE]
        top_songs = Song.objects.order_by("-view_count")[:PAGE_SIZE]

        new_songs_serializer = SongSerializer(
            new_songs, many=True, context={"request": request}
        )
        top_songs_serializer = SongSerializer(
            top_songs, many=True, context={"request": request}
        )

        banners = Banner.objects.all()
        banners_serializer = BannerSerializer(
            banners, many=True, context={"request": request}
        )

        combined_data = {
            "total": total,
            "new_songs": new_songs_serializer.data,
            "top_songs": top_songs_serializer.data,
            "banners": banners_serializer.data,
        }

        return Response(combined_data)


class IncreaseViewAPIView(APIView):

    serializer_class = IncreaseViewSerializer

    @swagger_auto_schema(request_body=IncreaseViewSerializer)
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        song_id = serializer.validated_data.get("song_id")
        try:
            song = Song.objects.get(id=song_id)
        except Exception as e:
            return Response(
                {"message": "not found song"}, status=status.HTTP_400_BAD_REQUEST
            )

        song.view_count += 1
        song.save()
        print("[user play]", song.title)
        return Response(
            {"song": song.title, "view_count": song.view_count},
            status=status.HTTP_200_OK,
        )
