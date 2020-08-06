import json
from django.test import TestCase, Client
from apps.books.models import Book, BookSerializer


class SerializerTests(TestCase):
    def setUp(self) -> None:
        self.JSON_FILE = 'volumes.json'

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
        self.client = Client()

    def test_list_view_loads(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)

    def test_detail_view_existing_book_loads(self):
        book_id = Book.objects.first().id

        response = self.client.get('/books/%s/' % (str(book_id)))
        self.assertEqual(response.status_code, 200)



