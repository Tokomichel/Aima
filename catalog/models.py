from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField()
    cover_url = models.URLField()

    def __str__(self):
        return self.title

class Track(models.Model):
    title = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    duration = models.FloatField()
    file_url = models.CharField(max_length=200)

    def __str__(self):
        return self.title