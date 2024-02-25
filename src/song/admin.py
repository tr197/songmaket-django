from django.contrib import admin
from song.models import Banner

class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    # list_filter = ('title',)
    # search_fields = ['title',]

admin.site.register(Banner, BannerAdmin)
