# Generated by Django 5.0.4 on 2024-04-07 17:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='category/images/')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('featured_image', models.ImageField(upload_to='place/images/')),
                ('place_field', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('is_deleted', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='places.category')),
            ],
            options={
                'db_table': 'place',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery/images/')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='places.place')),
            ],
            options={
                'db_table': 'gallery',
            },
        ),
    ]
