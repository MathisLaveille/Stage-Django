# Generated by Django 5.0.6 on 2024-05-28 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_band_active_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='year_formed',
            field=models.IntegerField(default=2000)
        ),
    ]