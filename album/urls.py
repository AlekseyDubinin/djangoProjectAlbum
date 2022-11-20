
from django.urls import path, include

from album.views import AlbumView, AlbumTablView

urlpatterns = [
    path('api/album/', AlbumView.as_view()),
    path('album/', AlbumTablView.as_view(), name='album'),

]