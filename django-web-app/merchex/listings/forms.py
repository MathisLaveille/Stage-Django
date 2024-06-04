from django import forms
from listings.models import Band
from .models import Band, Listing

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre email'}))
    message = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Votre message'}))

class BandForm(forms.ModelForm):
   class Meta:
     model = Band
     exclude = ('active', 'official_homepage')

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'
