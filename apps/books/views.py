from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book, BookSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['published_date']
    ordering = ['title']


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
