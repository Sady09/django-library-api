from rest_framework import serializers
from api.models import Book

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['titulo', 'autor', 'ano_de_leitura', 'nota', 'comentario']