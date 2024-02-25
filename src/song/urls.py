from django.urls import path
from song.views import SongListAPIView, SongSearchAPIView, SongHomeAPIView

urlpatterns = [
    path("home/", SongHomeAPIView.as_view()),
    path("songs/", SongListAPIView.as_view()),
    path("songs-search/", SongSearchAPIView.as_view()),
]
