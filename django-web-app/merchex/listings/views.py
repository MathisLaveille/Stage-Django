from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from listings.models import Band, Listing
from listings.models import Listing
from listings.forms import ContactUsForm, BandForm, ContactUsForm
from django.core.mail import send_mail
from .forms import BandForm, ListingForm
from django.contrib import messages
from django.shortcuts import render
from .models import Band
from django_tables2 import RequestConfig
from .tables import BandTable
from .tables import ListingTable
from django_tables2 import SingleTableView

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

class band_list2(SingleTableView):
    model = Band
    table_class = BandTable
    template_name = 'listings/band_list2.html'

class listing_list2(SingleTableView):
    model = Listing
    table_class = ListingTable
    template_name = 'listings/listing_list2.html'

def band_detail(request, id):
    #bands = Band.objects.get(pk=id)
    bands = get_object_or_404(Band, pk=id)
    return render(request, 'listings/band_detail.html', {'band': bands})

def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing_list.html', {'listings': listings})

def listing_detail(request, id):
    listing = get_object_or_404(Listing, id=id)
    return render(request, 'listings/listing_detail.html', {'listing': listing})

def about(request):
    bands = Band.objects.all()
    return render(request, 'listings/about.html', {'bands': bands})

def contact(request):

    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
        return redirect('email_sent')

    else:
        form = ContactUsForm()

    return render(request,
                  'listings/contact.html',
            {'form': form})

def email_sent(request):
    return render(request, 'listings/email_sent.html')

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)

        if form.is_valid():
            band = form.save()
            return redirect('band_detail', band.id)

    else:
        form = BandForm()

    return render(request,
            'listings/band_create.html',
            {'form': form})

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect('listing_detail', listing.id)  # Assurez-vous d'avoir une vue listing_detail
    else:
        form = ListingForm()

    return render(request, 'listings/listing_create.html', {'form': form})

def band_update(request, id):
    band = get_object_or_404(Band, id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band_detail', id=band.id)
    else:
        form = BandForm(instance=band)

    return render(request, 'listings/band_update.html', {'form': form})

def listing_update(request, id):
    listing = get_object_or_404(Listing, id=id)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listing_detail', id=listing.id)
    else:
        form = ListingForm(instance=listing)

    return render(request, 'listings/listing_update.html', {'form': form})

def band_delete(request, id):
    band = get_object_or_404(Band, id=id)

    if request.method == 'POST':
        band.delete()
        messages.success(request, f'Le groupe "{band.name}" a été supprimé avec succès.')
        return redirect('band_list')

    return render(request, 'listings/band_delete.html', {'band': band})

def listing_delete(request, id):
    listing = Listing.objects.get(id=id)

    if request.method == 'POST':
        listing.delete()
        messages.success(request, 'Listing supprimé avec succès.')
        return redirect('listing_list')  # Correction du nom de la redirection

    return render(request, 'listings/listing_delete.html', {'listing': listing})
