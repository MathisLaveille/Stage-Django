import django_tables2 as tables
from django.utils.translation import gettext as _
from .models import Typologie, Place, Type_connexion, Provider, Type_equipment, Brand, Equipment, Network, Platform, Software
from django.urls import reverse

class TypologieTable(tables.Table):
    name = tables.LinkColumn('typologie_update', args=[tables.A('pk')], verbose_name=_('typology'))

    class Meta:
        model = Typologie
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'description')

class Type_connexionTable(tables.Table):
    name = tables.LinkColumn('type_connexion_update', args=[tables.A('pk')], verbose_name=_('Connection type'))

    class Meta:
        model = Type_connexion
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'description')

class PlatformTable(tables.Table):
    name = tables.LinkColumn('platform_update', args=[tables.A('pk')], verbose_name=_('Platforme'))

    class Meta:
        model = Platform
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'description')

class Type_equipmentTable(tables.Table):
    name = tables.LinkColumn('type_equipment_update', args=[tables.A('pk')], verbose_name=_("Equipment type"))

    class Meta:
        model = Type_equipment
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'description')

class EquipmentTable(tables.Table):
    name = tables.LinkColumn('equipment_update', args=[tables.A('pk')], verbose_name=_("equipment"))

    class Meta:
        model = Equipment
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'place', 'type_equipment', 'brand', 'quantity', 'eligible', 'description', 'parent')

class NetworkTable(tables.Table):
    connection_type = tables.LinkColumn('network_update', args=[tables.A('pk')], verbose_name=_("connection_type"))

    class Meta:
        model = Network
        template_name = "django_tables2/bootstrap.html"
        fields = ('connection_type','place', 'provider', 'brand', 'rank', 'rescue', 'description')

class SoftwareTable(tables.Table):
    name = tables.LinkColumn('software_update', args=[tables.A('pk')], verbose_name=_("Software"))

    class Meta:
        model = Software
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'place', 'version', 'administrator', 'platform', 'description')

class ProviderTable(tables.Table):
    brand = tables.LinkColumn('provider_update', args=[tables.A('pk')], verbose_name=_('Supplier'))

    class Meta:
        model = Provider
        template_name = "django_tables2/bootstrap.html"
        fields = ('brand', 'description')

class BrandTable(tables.Table):
    brand = tables.LinkColumn('brand_update', args=[tables.A('pk')], verbose_name=_('brand'))

    class Meta:
        model = Brand
        template_name = "django_tables2/bootstrap.html"
        fields = ('brand', 'description')

class PlaceTable(tables.Table):
    name = tables.LinkColumn('place_update', args=[tables.A('pk')], verbose_name=_('Site'))
    typologie_name = tables.Column(accessor='typologie.name', verbose_name='Typologie')

    class Meta:
        model = Place
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'place', 'population', 'typology', 'latitude', 'longitude', 'description')