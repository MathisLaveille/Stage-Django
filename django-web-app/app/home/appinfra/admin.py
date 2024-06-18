from django.contrib import admin
from .models import Typologie, Place, Network

class TypologieAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'population', 'typologie', 'latitude', 'longitude', 'description')

class NetworkAdmin(admin.ModelAdmin):
    list_display = ('place', 'type_connection', 'provider', 'rank')

admin.site.register(Typologie, TypologieAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Network, NetworkAdmin)
