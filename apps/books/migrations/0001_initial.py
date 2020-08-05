# Generated by Django 3.1 on 2020-08-04 23:23

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('authors', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20), size=None)),
                ('published_date', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('categories', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20, null=True), blank=True, null=True, size=None)),
                ('average_rating', models.PositiveIntegerField(default=0)),
                ('ratings_count', models.PositiveIntegerField(default=0)),
                ('thumbnail', models.CharField(blank=True, max_length=2083, null=True)),
            ],
        ),
    ]