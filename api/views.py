from django.shortcuts import render
from rest_framework import viewsets
from api.models import Book
from config.serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer