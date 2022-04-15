from django.db import models

# Create your models here.
class Lyrics(models.Model):
    #song = models.OnetoOneField(Song)
    title = models.CharField(max_length=64)
    text = models.CharField(max_length=2048)
    