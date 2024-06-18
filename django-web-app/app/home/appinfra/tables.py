import django_tables2 as tables
from .models import Typologie, Place, Type_connexion, Provider, Type_equipment, Brand, Equipment, Network, Platform, Software
from django.urls import reverse

class TypologieTable(tables.Table):
    name = tables.LinkColumn('typologie_update', args=[tables.A('pk')], verbose_name='Typologie')

    class Meta:
        model = Typologie
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'description')

class Type_connexionTable(tables.Table):
    name = tables.LinkColumn('type_connexion_update', args=[tables.A('pk')], verbose_name='Type de connexion')

    class Meta:
        model = Type_connexion
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'description')

class PlatformTable(tables.Table):
    name = tables.LinkColumn('platform_update', args=[tables.A('pk')], verbose_name='Platforme')

    class Meta:
        model = Platform
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'description')

class Type_equipmentTable(tables.Table):
    name = tables.LinkColumn('type_equipment_update', args=[tables.A('pk')], verbose_name="Type d'equipment")

    class Meta:
        model = Type_equipment
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'description')

class EquipmentTable(tables.Table):
    name = tables.LinkColumn('equipment_update', args=[tables.A('pk')], verbose_name="nom-équipment")

    class Meta:
        model = Equipment
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'type_equipment', 'place', 'quantity', 'brand', 'eligible', 'description', 'parent')

class NetworkTable(tables.Table):
    type_connection = tables.LinkColumn('network_update', args=[tables.A('pk')], verbose_name="Connexion")

    class Meta:
        model = Network
        template_name = "django_tables2/bootstrap.html"
        fields = ('type_connection','place', 'rank', 'rescue', 'brand', 'provider', 'description')

class SoftwareTable(tables.Table):
    name = tables.LinkColumn('software_update', args=[tables.A('pk')], verbose_name="Logiciel")

    class Meta:
        model = Software
        template_name = "django_tables2/bootstrap.html"
        fields = ('name','version', 'administrator', 'place', 'description', 'platform')

class ProviderTable(tables.Table):
    marque = tables.LinkColumn('provider_update', args=[tables.A('pk')], verbose_name='Fournisseur')

    class Meta:
        model = Provider
        template_name = "django_tables2/bootstrap.html"
        fields = ('marque', 'description')

class BrandTable(tables.Table):
    marque = tables.LinkColumn('brand_update', args=[tables.A('pk')], verbose_name='Marque')

    class Meta:
        model = Brand
        template_name = "django_tables2/bootstrap.html"
        fields = ('marque', 'description')

class PlaceTable(tables.Table):
    name = tables.LinkColumn('place_update', args=[tables.A('pk')], verbose_name='Site')
    typologie_name = tables.Column(accessor='typologie.name', verbose_name='Typologie')

    class Meta:
        model = Place
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'place', 'population', 'latitude', 'longitude', 'description', 'typologie_name')