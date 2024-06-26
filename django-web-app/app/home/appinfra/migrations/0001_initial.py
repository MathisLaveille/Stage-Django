# Generated by Django 5.0.6 on 2024-06-19 14:25

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100, verbose_name='brand')),
                ('description', models.CharField(max_length=1000, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('place', models.CharField(max_length=100, verbose_name='place')),
                ('population', models.IntegerField(verbose_name='population')),
                ('latitude', models.CharField(max_length=100, verbose_name='latitude')),
                ('longitude', models.CharField(max_length=100, verbose_name='longitude')),
                ('description', models.CharField(max_length=1000, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.CharField(max_length=1000, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100, verbose_name='brand')),
                ('description', models.CharField(max_length=1000, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='Type_connexion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.CharField(max_length=1000, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='Type_equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.CharField(max_length=1000, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='Typologie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.CharField(max_length=1000, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('version', models.CharField(max_length=100, verbose_name='version')),
                ('administrator', models.CharField(max_length=100, verbose_name='administrator')),
                ('description', models.CharField(max_length=1000, verbose_name='description')),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appinfra.place', verbose_name='place')),
                ('platform', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appinfra.platform', verbose_name='platform')),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9)], verbose_name='rank')),
                ('rescue', models.BooleanField(default=False, verbose_name='rescue')),
                ('description', models.CharField(max_length=1000, verbose_name='description')),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appinfra.brand', verbose_name='brand')),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appinfra.place', verbose_name='place')),
                ('provider', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appinfra.provider', verbose_name='provider')),
                ('connection_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appinfra.type_connexion', verbose_name='connection_type')),
            ],
            options={
                'ordering': ['rank'],
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('quantity', models.IntegerField(default=0, verbose_name='quantity')),
                ('eligible', models.BooleanField(default=False, verbose_name='eligible')),
                ('description', models.CharField(blank=True, max_length=1024, null=True, verbose_name='description')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='appinfra.brand', verbose_name='brand')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='appinfra.equipment', verbose_name='parent')),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appinfra.place', verbose_name='place')),
                ('type_equipment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appinfra.type_equipment', verbose_name='type_equipment')),
            ],
        ),
        migrations.AddField(
            model_name='place',
            name='typology',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appinfra.typologie', verbose_name='typology'),
        ),
    ]
