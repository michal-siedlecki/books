from django_filters import rest_framework as filters
from .models import Book



class AuthorFilter(filters.FilterSet):
    authors = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Book
        fields = ('authors', )
