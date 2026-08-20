from django.contrib import admin
from django.contrib.admin import site

from catalog.models import Album, Artist, Track


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')
    search_fields = ('name', 'bio')

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'release_date')
    search_fields = ('title', 'artist__name')
    list_filter = ('release_date',)

class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'duration')
    search_fields = ('title', 'album__title')
    list_filter = ('album',)

# Register your models here.

site.register(Artist, ArtistAdmin)
site.register(Album, AlbumAdmin)
site.register(Track, TrackAdmin)