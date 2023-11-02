from rest_framework import serializers
from .models import *

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

class JournalistCriticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalistCritics
        fields = '__all__'

class ModelBertBmusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelBertBmus
        fields = '__all__'


class ModelDistilbertBmcssSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelDistilbertBmcss
        fields = '__all__'

class SpectatorCriticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpectatorCritics
        fields = '__all__'