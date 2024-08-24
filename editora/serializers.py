from rest_framework import serializers
from .models import Autor, Livro

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = [
            'nome',
            'email'
        ]
        
class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = [
            'titulo',
            'data_publicacao',
            'autor'
        ]