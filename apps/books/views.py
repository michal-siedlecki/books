from django.db.models import QuerySet
from rest_framework import generics
from .models import Book, BookSerializer


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned books to a given authors or published date,
        by filtering against a `author` and `published_date` query parameters in the URL.
        """
        queryset = Book.objects.all()
        ordering = self.request.query_params.get('sort', None)
        authors = self.request.query_params.getlist('author', None)
        published_date = self.request.query_params.get('published_date', None)
        if published_date:
            queryset = queryset.filter(published_date=published_date)
        if authors:
            queryset_list = [queryset.filter(authors__icontains=author) for author in authors if author is not None]
            queryset = QuerySet.union(*queryset_list)
        if ordering:
            queryset = queryset.order_by(ordering)
        return queryset


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
