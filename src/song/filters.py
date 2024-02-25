from django_filters import FilterSet, CharFilter, OrderingFilter
from .models import Song


class SongFilter(FilterSet):
    title = CharFilter(lookup_expr="icontains")
    artist_name = CharFilter(field_name="artist__name", lookup_expr="icontains")
    artist = CharFilter(field_name="artist", lookup_expr="exact")
    ordering = OrderingFilter(fields=("title", "created_at"))

    class Meta:
        model = Song
        fields = ["title", "artist_name"]
