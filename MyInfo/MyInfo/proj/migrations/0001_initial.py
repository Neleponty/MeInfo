# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-06 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attractions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('coord', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'attractions',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'managed': True,
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='CategoriesLinks',
            fields=[
                ('parent_id', models.IntegerField()),
                ('child_id', models.IntegerField()),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'managed': True,
                'db_table': 'categories_links',
            },
        ),
        migrations.CreateModel(
            name='LocationNewsEvent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('coord', models.TextField()),
            ],
            options={
                'managed': True,
                'db_table': 'location_news_event',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pub_date', models.DateTimeField()),
                ('name', models.CharField(max_length=500)),
                ('header', models.CharField(max_length=5000)),
                ('content', models.TextField()),
                ('is_fav', models.BooleanField()),
                ('likes', models.IntegerField()),
                ('scale', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'news',
            },
        ),
        migrations.CreateModel(
            name='NewsPhotos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'managed': True,
                'db_table': 'news_photos',
            },
        ),
        migrations.CreateModel(
            name='Opinions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pub_date', models.DateTimeField()),
                ('title', models.TextField()),
                ('headline', models.TextField(blank=True, null=True)),
                ('image', models.TextField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'opinions',
            },
        ),
        migrations.CreateModel(
            name='OpinionsImages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'managed': True,
                'db_table': 'opinions_images',
            },
        ),
        migrations.CreateModel(
            name='OpinionsLocations',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('opinion_id', models.IntegerField()),
                ('coord', models.TextField()),
            ],
            options={
                'managed': True,
                'db_table': 'opinions_locations',
            },
        ),
        migrations.CreateModel(
            name='OpinionsToTags',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'managed': True,
                'db_table': 'opinionstotags',
            },
        ),
        migrations.CreateModel(
            name='PhotoAlbumsTitle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'photoalbums_title',
            },
        ),
        migrations.CreateModel(
            name='PhotosInAlbums',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'managed': True,
                'db_table': 'photos_in_albums',
            },
        ),
        migrations.CreateModel(
            name='PhotosUrls',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=300)),
            ],
            options={
                'managed': True,
                'db_table': 'photos_urls',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
            options={
                'managed': True,
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='TourPoint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('coordinates', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'tour_point',
            },
        ),
        migrations.CreateModel(
            name='Tours',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'tours',
            },
        ),
        migrations.CreateModel(
            name='ToursToPoints',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'managed': True,
                'db_table': 'tours_to_points',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('login', models.TextField()),
                ('name', models.TextField(blank=True, null=True)),
                ('hashpass', models.TextField()),
            ],
            options={
                'managed': True,
                'db_table': 'users',
            },
        ),
    ]
