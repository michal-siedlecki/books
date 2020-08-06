# Generated by Django 3.1 on 2020-08-06 10:58
import json
from django.db import migrations
from apps.books.models import BookSerializer


JSON_FILE = 'volumes.json'

def load_data(apps, schema_editor):
    Book = apps.get_model('books', 'Book')
    with open(JSON_FILE) as datafile:
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


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
