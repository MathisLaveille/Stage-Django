# Generated by Django 5.0.6 on 2024-06-18 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appinfra', '0015_alter_equipment_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='software',
        ),
    ]