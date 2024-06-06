from django.contrib import admin
from .models import Typologie, Place

class TypologieAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'population', 'typologie', 'latitude', 'longitude', 'description')

admin.site.register(Typologie, TypologieAdmin)
admin.site.register(Place, PlaceAdmin)
