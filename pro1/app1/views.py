from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .serializers import SongSerializer, Song
from rest_framework.filters import SearchFilter


class SongInfo(CreateAPIView, ListAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['name']


class SongDetails(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()





