from django.urls import path, include
from . import views
from .views import *
from .models import *
from .serializer import *

urlpatterns = [
    path('list-film/', FilmList.as_view(), name='list-film'),
    path('create-film/', FilmCreate.as_view(), name='create-film'),
    path('list-commentaire/', SpectatorCriticsList.as_view(), name='list-commentaire'),
    path('crud-commentaire/', SpectatorCriticsCrud.as_view(), name='crud-commentaire'),
    path('api/start_scraping/', views.scrapping, name='start_scraping'),
    path('api/predict/', views.predict, name='predict')
]