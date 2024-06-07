from django import forms
from .models import Typologie, Place, Type_connexion,Type_equipment, Brand, Provider, Equipment

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre email'}))
    message = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Votre message'}))

class TypologieForm(forms.ModelForm):
   class Meta:
     model = Typologie
     fields = '__all__'

class Type_connexionForm(forms.ModelForm):
   class Meta:
     model = Type_connexion
     fields = '__all__'

class Type_equipmentForm(forms.ModelForm):
   class Meta:
     model = Type_equipment
     fields = '__all__'

class EquipmentForm(forms.ModelForm):
   class Meta:
     model = Equipment
     fields = '__all__'

class ProviderForm(forms.ModelForm):
   class Meta:
     model = Provider
     fields = '__all__'

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'