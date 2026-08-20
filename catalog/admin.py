from django.contrib import admin
from django.contrib.admin import site

from catalog.models import Artist


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')
    search_fields = ('name', 'bio')

# Register your models here.

site.register(Artist, ArtistAdmin)