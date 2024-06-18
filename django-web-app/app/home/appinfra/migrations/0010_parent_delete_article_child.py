# Generated by Django 5.0.6 on 2024-06-18 06:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appinfra', '0009_alter_software_place_alter_software_platform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('parent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='appinfra.parent')),
                ('child_only_field', models.CharField(max_length=64)),
            ],
            bases=('appinfra.parent',),
        ),
    ]
