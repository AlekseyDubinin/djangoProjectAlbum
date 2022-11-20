from django.db import models
# Track с полем name в виде строки, и с полем album указывающим на модель Albu


class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Артист"
        verbose_name_plural = "Артисты"


class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.name}[{self.year}]'

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"


class Track(models.Model):
    name = models.CharField(max_length=200)
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Трек"
        verbose_name_plural = "Треки"


