from rest_framework.serializers import ModelSerializer
from .models import MovieModel

class MovieSerialaizer(ModelSerializer):
    class Meta:
        model = MovieModel
        fields = '__all__'
