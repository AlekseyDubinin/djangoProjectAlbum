from rest_framework import serializers
from album.models import Album, Artist, Track


class AlbumSerializer(serializers.ModelSerializer):
    artist = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name"
    )
    tracks = serializers.StringRelatedField(many=True)
    album = serializers.SerializerMethodField()

    def get_album(self, obj):
        return str(obj)

    class Meta:
        model = Album
        fields = ["album", "name", "artist", "tracks"]
