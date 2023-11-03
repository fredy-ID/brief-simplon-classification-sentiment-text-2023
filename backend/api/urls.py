from django.urls import path, include
from . import views
from .views import *
from .models import *
from .serializer import *

urlpatterns = [
    path('listFilm/', FilmList.as_view(), name='list-film'),
    path('createFilm/', FilmCreate.as_view(), name='create-film'),
    path('listCom/', CriticsList.as_view(), name='list-com')
]