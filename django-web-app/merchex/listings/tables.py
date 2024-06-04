import django_tables2 as tables
from .models import Band
from .models import Listing
from django.urls import reverse

class BandTable(tables.Table):
    name = tables.LinkColumn('band_detail', args=[tables.A('pk')], verbose_name='Detail')

    class Meta:
        model = Band
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'genre', 'year_formed', 'biography', 'active', 'official_homepage')

class ListingTable(tables.Table):
    title = tables.LinkColumn('listing_detail', args=[tables.A('pk')], verbose_name='Detail')

    class Meta:
        model = Listing
        template_name = "django_tables2/bootstrap.html"
        fields = ('title', 'description', 'sold', 'type', 'year')