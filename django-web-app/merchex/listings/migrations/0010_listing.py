# Generated by Django 5.0.6 on 2024-05-28 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_alter_band_year_formed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
