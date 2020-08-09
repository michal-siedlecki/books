from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .filters import AuthorFilter
from .models import Book, BookSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = AuthorFilter
    filterset_fields = ['published_date', 'title', 'average_rating', 'ratings_count', 'authors']


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
