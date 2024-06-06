from django import forms
from appinfra.models import Typologie
from .models import Typologie, Place

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre email'}))
    message = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Votre message'}))

class TypologieForm(forms.ModelForm):
   class Meta:
     model = Typologie
     fields = '__all__'

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'
