from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=256)
    artist = models.CharField(max_length=128)
    albumTitle = models.CharField(max_length=256,blank=True)
    albumArt = models.CharField(max_length=128,default="/music.jpg")
    genre = models.CharField(max_length=64,blank=True)
    media = models.CharField(max_length=256,blank=True)
    isPlayable = models.BooleanField(default=False)
    preview = models.CharField(max_length=256,blank=True)
    lyrics = models.ForeignKey('lyrics_api.Lyrics', on_delete=models.CASCADE,null=True)