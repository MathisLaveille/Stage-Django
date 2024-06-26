from django.contrib import admin
from .models import Typologie, Place, Network

class TypologieAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'population', 'typology', 'latitude', 'longitude', 'description')

class NetworkAdmin(admin.ModelAdmin):
    list_display = ('place', 'connection_type', 'provider', 'brand', 'rank', 'rescue', 'description')

admin.site.register(Typologie, TypologieAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Network, NetworkAdmin)
