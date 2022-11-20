from django.contrib import admin

from album.models import Album, Artist, Track

admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Track)
