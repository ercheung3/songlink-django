from django.db import models

# Create your models here.
class Lyrics(models.Model):
    #song = models.OnetoOneField(Song)
    text= models.TextField