# Generated by Django 5.0.6 on 2024-06-07 09:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appinfra', '0003_brand_provider_type_connexion_type_equipment_network_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='network',
            old_name='primary_brand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='network',
            old_name='primary_provider',
            new_name='provider',
        ),
        migrations.RenameField(
            model_name='network',
            old_name='primary_type_connection',
            new_name='type_connection',
        ),
        migrations.RemoveField(
            model_name='network',
            name='secondary_brand',
        ),
        migrations.RemoveField(
            model_name='network',
            name='secondary_provider',
        ),
        migrations.RemoveField(
            model_name='network',
            name='secondary_type_connection',
        ),
        migrations.AddField(
            model_name='network',
            name='rank',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='network',
            name='rescue',
            field=models.BooleanField(default=False),
        ),
    ]
