# Generated by Django 5.0.4 on 2024-04-10 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
