import json
from django.test import TestCase
from apps.books.models import BookSerializer


class SerializerTests(TestCase):
    def setUp(self) -> None:
        self.JSON_FILE = 'volumes.json'

    def test_load_data(self):
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
                print("-------------")
                print(book_serializer.validated_data)
                print("-------------")
