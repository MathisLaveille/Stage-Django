# Generated by Django 5.0.6 on 2024-06-18 10:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appinfra', '0012_alter_equipment_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='software',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='appinfra.software'),
        ),
    ]
