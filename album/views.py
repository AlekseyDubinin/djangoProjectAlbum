from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from rest_framework.generics import ListAPIView

from album.serializers import AlbumSerializer
from album.models import Album
import requests


class AlbumView(ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumTablView(TemplateView):
    template_name = "albom.html"

    def get_context_data(self, **kwargs):
        albums = requests.get('http://localhost:8000/api/album/').json()
        context = {
            'albums': albums
        }
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        name_album = request.GET.get('sort')
        if name_album == 'name_sort':
            context['albums'] = sorted(context['albums'], key=lambda d: d['name'])
        elif name_album == 'artist_sort':
            context['albums'] = sorted(context['albums'], key=lambda d: d['artist'])
        return render(request, self.template_name, context)





