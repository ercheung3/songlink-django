from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import SongSerializer
from .models import Song

class SongList(generics.ListCreateAPIView):
    #How django will retrieve all objects
    queryset = Song.objects.all().order_by('id')
    #Tells django what serializer to use
    serializer_class = SongSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all().order_by('id')
    serializer_class = SongSerializer