# Generated by Django 5.0.4 on 2024-04-10 18:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_gallery_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='places', to='places.category'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='featured_image',
            field=models.ImageField(blank=True, upload_to='place/images/'),
        ),
        migrations.AlterField(
            model_name='place',
            name='is_deleted',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_field',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
