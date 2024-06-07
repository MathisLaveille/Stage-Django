import django_tables2 as tables
from .models import Typologie, Place, Type_connexion, Provider, Type_equipment, Brand, Equipment
from django.urls import reverse

class TypologieTable(tables.Table):
    name = tables.LinkColumn('typologie_detail', args=[tables.A('pk')], verbose_name='Typologie')

    class Meta:
        model = Typologie
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'description')

class Type_connexionTable(tables.Table):
    name = tables.LinkColumn('type_connexion_detail', args=[tables.A('pk')], verbose_name='Type de connexion')

    class Meta:
        model = Type_connexion
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'description')

class Type_equipmentTable(tables.Table):
    name = tables.LinkColumn('type_equipment_detail', args=[tables.A('pk')], verbose_name="Type d'equipment")

    class Meta:
        model = Type_equipment
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'description')

class EquipmentTable(tables.Table):
    id = tables.LinkColumn('Equipment_detail', args=[tables.A('pk')], verbose_name="Equipment")

    class Meta:
        model = Equipment
        template_name = "django_tables2/bootstrap.html"
        fields = ('quantity', 'eligible', 'description', 'brand_id', 'place_id', 'type_equipment_id')

class ProviderTable(tables.Table):
    marque = tables.LinkColumn('provider_detail', args=[tables.A('pk')], verbose_name='Fournisseur')

    class Meta:
        model = Provider
        template_name = "django_tables2/bootstrap.html"
        fields = ('marque', 'description')

class BrandTable(tables.Table):
    marque = tables.LinkColumn('brand_detail', args=[tables.A('pk')], verbose_name='Marque')

    class Meta:
        model = Brand
        template_name = "django_tables2/bootstrap.html"
        fields = ('marque', 'description')

class PlaceTable(tables.Table):
    name = tables.LinkColumn('place_detail', args=[tables.A('pk')], verbose_name='Site')
    typologie_name = tables.Column(accessor='typologie.name', verbose_name='Typologie')

    class Meta:
        model = Place
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'place', 'population', 'latitude', 'longitude', 'description', 'typologie_name')