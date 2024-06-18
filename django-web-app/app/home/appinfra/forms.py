from django import forms
from .models import Typologie, Place, Type_connexion,Type_equipment, Brand, Provider, Equipment, Network, Platform, Software

from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre email'}))
    message = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Votre message'}))

class TypologieForm(forms.ModelForm):
   class Meta:
     model = Typologie
     fields = '__all__'
     widgets = {
         'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la typologie'}),
         'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
     }

class Type_connexionForm(forms.ModelForm):
   class Meta:
     model = Type_connexion
     fields = '__all__'
     widgets = {
         'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du type de connexion'}),
         'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
     }

class Type_equipmentForm(forms.ModelForm):
   class Meta:
     model = Type_equipment
     fields = '__all__'
     widgets = {
         'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom du type d'équipment"}),
         'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
     }

class PlatformForm(forms.ModelForm):
   class Meta:
     model = Platform
     fields = '__all__'
     widgets = {
         'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la typologie'}),
         'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
     }

class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'
        widgets = {
            'marque': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du fournisseur'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
        widgets = {
            'marque': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la marque'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
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
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du site'}),
            'place': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la place'}),
            'population': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Population'}),
            'typologie': forms.Select(attrs={'class': 'form-control'}),
            'latitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Latitude'}),
            'longitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Longitude'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }

class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du logiciel'}),
            'version': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Version'}),
            'administrator': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom de l'administrateur"}),
            'platform': forms.Select(attrs={'class': 'form-control'}),
            'place': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }