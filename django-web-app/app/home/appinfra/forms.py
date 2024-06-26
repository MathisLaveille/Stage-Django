from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Typologie, Place, Type_connexion, Type_equipment, Brand, Provider, Equipment, Network, Platform, Software
from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Your name')}), label=_('Name'))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('Your email')}))
    message = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Your message')}))

class TypologieForm(forms.ModelForm):
    class Meta:
        model = Typologie
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Typology name')}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Typology description')}),
        }

class Type_connexionForm(forms.ModelForm):
    class Meta:
        model = Type_connexion
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Connection type name')}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Connection type description')}),
        }

class Type_equipmentForm(forms.ModelForm):
    class Meta:
        model = Type_equipment
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Equipment type name')}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Equipment type description')}),
        }

class PlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Platform name')}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Platform description')}),
        }

class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Provider name')}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Provider description')}),
        }

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Brand name')}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Brand description')}),
        }

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'

class NetworkForm(forms.ModelForm):
    class Meta:
        model = Network
        fields = '__all__'

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Site name')}),
            'place': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Place name')}),
            'population': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': _('Population')}),
            'typology': forms.Select(attrs={'class': 'form-control'}),
            'latitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Latitude')}),
            'longitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Longitude')}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Place description')}),
        }

class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Software name')}),
            'version': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Version')}),
            'administrator': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Administrator name')}),
            'platform': forms.Select(attrs={'class': 'form-control'}),
            'place': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Software description')}),
        }