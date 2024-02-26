from django.contrib import admin
from song.models import Artist, Song


class SongAdmin(admin.ModelAdmin):
    list_display = ("title", "artist", "view_count")
    list_filter = ("artist",)
    search_fields = [
        "title",
    ]


admin.site.register(Song, SongAdmin)
admin.site.register(Artist)
