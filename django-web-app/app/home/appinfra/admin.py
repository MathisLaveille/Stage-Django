from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Typologie, Place, Type_connexion, Type_equipment, Brand, Provider, Equipment, Network, Platform, Software

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active',)
    list_filter = ('role', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Informations', {'fields': ('role', 'phone_number')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'role', 'phone_number', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'email', 'role')
    ordering = ('username',)

class TypologieAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'population', 'typology', 'latitude', 'longitude', 'description')

class NetworkAdmin(admin.ModelAdmin):
    list_display = ('place', 'connection_type', 'provider', 'brand', 'rank', 'rescue', 'description')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Typologie, TypologieAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Network, NetworkAdmin)
