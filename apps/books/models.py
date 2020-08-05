from django.contrib.postgres.fields import ArrayField
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    authors = ArrayField(models.CharField(max_length=20, blank=True))
    published_date = models.PositiveSmallIntegerField(blank=True, null=True)
    categories = ArrayField(models.CharField(max_length=20, blank=True, null=True), blank=True, null=True)
    average_rating = models.PositiveIntegerField(default=0)
    ratings_count = models.PositiveIntegerField(default=0)
    thumbnail = models.CharField(max_length=2083, blank=True, null=True)

