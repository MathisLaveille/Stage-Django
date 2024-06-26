# Generated by Django 5.0.6 on 2024-05-28 09:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_alter_band_year_formed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='year_formed',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2021)]),
        ),
    ]
