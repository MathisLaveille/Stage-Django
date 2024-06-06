from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from appinfra.models import Typologie, Place
from appinfra.models import Place
from appinfra.forms import ContactUsForm, TypologieForm, ContactUsForm
from django.core.mail import send_mail
from .forms import TypologieForm, PlaceForm
from django.contrib import messages
from django.shortcuts import render
from .models import Typologie
from django_tables2 import RequestConfig
from .tables import TypologieTable
from .tables import PlaceTable
from django_tables2 import SingleTableView
from django.shortcuts import render, redirect
from .forms import PlaceForm
from .models import Place

def accueil(request):
    return render(request,'accueil.html')

class typologie_list(SingleTableView):
    model = Typologie
    table_class = TypologieTable
    template_name = 'typologie_list.html'

class place_list(SingleTableView):
    model = Place
    table_class = PlaceTable
    template_name = 'place_list.html'

def typologie_detail(request, id):
    typologies = get_object_or_404(Typologie, pk=id)
    return render(request, 'typologie_detail.html', {'typologie': typologies})

def place_detail(request, id):
    places = get_object_or_404(Place, pk=id)
    return render(request, 'place_detail.html', {'place': places})

def typologie_create(request):
    if request.method == 'POST':
        form = TypologieForm(request.POST)

        if form.is_valid():
            typologie = form.save()
            return redirect('typologie_detail', typologie.id)

    else:
        form = TypologieForm()

    return render(request,
            'typologie_create.html',
            {'form': form})

def place_create(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)

        if form.is_valid():
            place = form.save()
            return redirect('place_detail', place.id)

    else:
        form = PlaceForm()

    return render(request,
            'place_create.html',
            {'form': form})
def typologie_update(request, id):
    typologie = get_object_or_404(Typologie, id=id)

    if request.method == 'POST':
        form = TypologieForm(request.POST, instance=typologie)
        if form.is_valid():
            form.save()
            return redirect('typologie_detail', id=typologie.id)
    else:
        form = TypologieForm(instance=typologie)

    return render(request, 'typologie_update.html', {'form': form})

def place_update(request, id):
    place = get_object_or_404(Place, id=id)

    if request.method == 'POST':
        form = PlaceForm(request.POST, instance=place)
        if form.is_valid():
            form.save()
            return redirect('place_detail', id=place.id)
    else:
        form = PlaceForm(instance=place)

    return render(request, 'place_update.html', {'form': form})

def typologie_delete(request, id):
    typologie = get_object_or_404(Typologie, id=id)

    if request.method == 'POST':
        typologie.delete()
        messages.success(request, f'Le groupe "{typologie.name}" a été supprimé avec succès.')
        return redirect('typologie_list')

    return render(request, 'typologie_delete.html', {'typologie': typologie})

def place_delete(request, id):
    place = get_object_or_404(Place, id=id)

    if request.method == 'POST':
        place.delete()
        messages.success(request, f'Le groupe "{place.name}" a été supprimé avec succès.')
        return redirect('place_list')

    return render(request, 'place_delete.html', {'place': place})

def typologie(request):
    typologies = Typologie.objects.all()
    return render(request, 'typologie_list.html', {'typologies': typologies})

def place(request):
    places = Place.objects.all()
    return render(request, 'place_list.html', {'places': places})

def about(request):
    return render(request,'about.html')

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
                  'contact.html',
            {'form': form})

def email_sent(request):
    return render(request, '/email_sent.html')