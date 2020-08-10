import json
from django.test import TestCase
from apps.books.models import Book, BookSerializer
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class SerializerTests(TestCase):
    def setUp(self) -> None:
        self.JSON_FILE = 'initial_data/volumes.json'

    def test_load_data(self):
        books_count_initial = len(Book.objects.all())
        with open(self.JSON_FILE) as datafile:
            objects = json.load(datafile)
            books = objects.get('items')
            for item in books:
                volume_info = item['volumeInfo']
                book = dict(
                    title=volume_info.get('title'),
                    authors=volume_info.get('authors'),
                    published_date=volume_info.get('publishedDate'),
                    categories=volume_info.get('categories'),
                    average_rating=volume_info.get('averageRating'),
                    ratings_count=volume_info.get('ratingsCount'),
                    thumbnail=volume_info['imageLinks']['thumbnail']
                )
                book_serializer = BookSerializer(data=book)
                book_serializer.is_valid(raise_exception=True)
                book_new = Book(**book_serializer.validated_data)
                book_new.save()
        objects_count = len(books)
        books_count = len(Book.objects.all()) - books_count_initial
        self.assertEqual(objects_count, books_count)


class APIViewsTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_list_view_loads_all_books(self):
        books_count_initial = len(Book.objects.all())
        response = self.client.get('/books')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('count'), books_count_initial)

    def test_detail_view_loads_exact_book(self):
        book_id = 1
        response = self.client.get('/books/%s' % book_id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('id'), book_id)

    def test_published_date_filter(self):
        published_date = 2012
        response = self.client.get('/books?published_date=2012')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('count'), len(Book.objects.filter(published_date=published_date)))

    def test_create_book(self):
        """
        Ensure we can create a new book object.
        """
        books_count_initial = len(Book.objects.all())
        url = reverse('books')
        data = {
            'title': 'My new book',
            'authors': ['Test user'],
            'published_date': 2020,
            'categories': ['Science fiction'],
            'average_rating': 0,
            'ratings_count': 0,
            'thumbnail': 'www.example.com/book.jpg'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), books_count_initial+1)
        self.assertEqual(Book.objects.get(title=data.get('title')).title, data.get('title'))

