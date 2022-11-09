from django.db import models
from datetime import datetime

# Create your models here.


class Artist(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    age = models.IntegerField()


class Song(models.Model):
    title = models.CharField(max_length=400)
    date_released = models.DateField(default=datetime.today)
    likes = models.IntegerField()
    artist_id = models.PositiveIntegerField()


class Lyric(models.Model):
    content = models.CharField(max_length=4000)
    song_id = models.PositiveIntegerField()
