from rest_framework import generics
from .models import *
from .serializer import *

class FilmList(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class FilmCreate(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class CriticsList(generics.ListAPIView):
    queryset = SpectatorCritics.objects.all()
    serializer_class = SpectatorCriticsSerializer