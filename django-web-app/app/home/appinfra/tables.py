import django_tables2 as tables
from .models import Typologie, Place
from django.urls import reverse

class TypologieTable(tables.Table):
    name = tables.LinkColumn('typologie_detail', args=[tables.A('pk')], verbose_name='Typologie')

    class Meta:
        model = Typologie
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'description')

class PlaceTable(tables.Table):
    name = tables.LinkColumn('place_detail', args=[tables.A('pk')], verbose_name='Site')

    class Meta:
        model = Place
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'place', 'population', 'latitude', 'longitude', 'description', 'typologie_id')