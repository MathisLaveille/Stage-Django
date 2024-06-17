# Generated by Django 5.0.6 on 2024-06-14 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appinfra', '0005_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterModelOptions(
            name='network',
            options={'ordering': ['rank']},
        ),
    ]