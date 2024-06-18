# Generated by Django 5.0.6 on 2024-06-18 07:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appinfra', '0010_parent_delete_article_child'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='appinfra.equipment'),
        ),
        migrations.DeleteModel(
            name='Child',
        ),
        migrations.DeleteModel(
            name='Parent',
        ),
    ]
