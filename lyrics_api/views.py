from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import LyricsSerializer
from .models import Lyrics

class LyricsList(generics.ListCreateAPIView):
    #How django will retrieve all objects
    queryset = Lyrics.objects.all().order_by('id')
    #Tells django what serializer to use
    serializer_class = LyricsSerializer

class LyricsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lyrics.objects.all().order_by('id')
    serializer_class = LyricsSerializer
    
