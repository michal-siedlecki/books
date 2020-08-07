import datetime

from django.contrib.postgres.fields import ArrayField
from django.db import models
from rest_framework import serializers


class Book(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    authors = ArrayField(models.CharField(max_length=250, blank=True, null=True), default=list, null=True)
    published_date = models.PositiveIntegerField(blank=True, null=True)
    categories = ArrayField(models.CharField(max_length=250, blank=True, null=True), default=list, null=True)
    average_rating = models.IntegerField(default=0, null=True, blank=True)
    ratings_count = models.IntegerField(default=0, null=True, blank=True)
    thumbnail = models.CharField(max_length=2083, blank=True, null=True)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def to_internal_value(self, data):
        try:
            data['published_date'] = datetime.datetime.strptime(str(data['published_date']), '%Y-%m-%d').year
        except ValueError:
            data['published_date'] = int(data['published_date'])

        if not isinstance(data['average_rating'], int):
            try:
                data['average_rating'] = int(data['average_rating'])
            except TypeError:
                data['average_rating'] = 0

        if not isinstance(data['ratings_count'], int):
            try:
                data['ratings_count'] = int(data['ratings_count'])
            except TypeError:
                data['ratings_count'] = 0

        return super().to_internal_value(data)
