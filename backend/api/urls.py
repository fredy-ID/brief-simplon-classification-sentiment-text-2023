from django.urls import path, include
from . import views
from .generics import *
from .models import *
from .serializer import *

urlpatterns = [
    path('listFilm/', FilmList.as_view(queryset=Film.objects.all(), serializer_class=FilmSerializer), name='film-list'),
    path('createFilm/', FilmCreate.as_view(queryset=Film.objects.all(), serializer_class=FilmSerializer), name='film-list')
]