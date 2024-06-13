from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from appinfra.models import Typologie, Place, Type_connexion, Provider, Type_equipment, Brand
from appinfra.forms import ContactUsForm, TypologieForm, ContactUsForm
from django.core.mail import send_mail
from .forms import TypologieForm, PlaceForm, Type_connexionForm, ProviderForm, Type_equipmentForm, BrandForm, \
    EquipmentForm, NetworkForm
from .tables import TypologieTable, PlaceTable, Type_connexionTable, ProviderTable, Type_equipmentTable, BrandTable, \
    EquipmentTable, NetworkTable
from django_tables2 import SingleTableView
from django.shortcuts import render, redirect
from .models import Place, Type_connexion, Typologie, Provider, Type_equipment, Brand, Equipment, Network
from django.contrib import messages
from django.core.mail import send_mail


def accueil(request):
    return render(request, 'autres/accueil.html')


class typologie_list(SingleTableView):
    model = Typologie
    table_class = TypologieTable
    template_name = 'typologie/typologie_list.html'


class place_list(SingleTableView):
    model = Place
    table_class = PlaceTable
    template_name = 'place/place_list.html'


class type_connexion_list(SingleTableView):
    model = Type_connexion
    table_class = Type_connexionTable
    template_name = 'type_connexion/type_connexion_list.html'


class type_equipment_list(SingleTableView):
    model = Type_equipment
    table_class = Type_equipmentTable
    template_name = 'type_equipment/type_equipment_list.html'

    def get_queryset(self):
        return super().get_queryset()

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()

        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(
                    self.object_list, "exists"
            ):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                raise Http404(
                    _("Empty list and “%(class_name)s.allow_empty” is False.")
                    % {
                        "class_name": self.__class__.__name__,
                    }
                )
        context = self.get_context_data()
        return self.render_to_response(context)


class equipment_list(SingleTableView):
    model = Equipment
    table_class = EquipmentTable
    template_name = 'equipment/equipment_list.html'


class network_list(SingleTableView):
    model = Network
    table_class = NetworkTable
    template_name = 'network/network_list.html'

class place_equipment_list(SingleTableView):
    model = Equipment
    table_class = EquipmentTable
    template_name = 'place_equipment/place_equipment_list.html'


class place_network_list(SingleTableView):
    model = Network
    table_class = NetworkTable
    template_name = 'place_network/place_network_list.html'

class provider_list(SingleTableView):
    model = Provider
    table_class = ProviderTable
    template_name = 'provider/provider_list.html'


class brand_list(SingleTableView):
    model = Brand
    table_class = BrandTable
    template_name = 'brand/brand_list.html'


def typologie_create(request):
    if request.method == 'POST':
        form = TypologieForm(request.POST)

        if form.is_valid():
            typologie = form.save()
            return redirect('typologie_update', typologie.id)

    else:
        form = TypologieForm()

    return render(request,
                  'typologie/typologie_create.html',
                  {'form': form})


def place_create(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)

        if form.is_valid():
            place = form.save()
            return redirect('place_update', place.id)

    else:
        form = PlaceForm()

    return render(request,
                  'place/place_create.html',
                  {'form': form})


def type_connexion_create(request):
    if request.method == 'POST':
        form = Type_connexionForm(request.POST)

        if form.is_valid():
            type_connexion = form.save()
            return redirect('type_connexion_update', type_connexion.id)

    else:
        form = Type_connexionForm()

    return render(request,
                  'type_connexion/type_connexion_create.html',
                  {'form': form})


def type_equipment_create(request):
    if request.method == 'POST':
        form = Type_equipmentForm(request.POST)

        if form.is_valid():
            type_equipment = form.save()
            return redirect('type_equipment_update', type_equipment.id)

    else:
        form = Type_equipmentForm()

    return render(request,
                  'type_equipment/type_equipment_create.html',
                  {'form': form})


def equipment_create(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)

        if form.is_valid():
            equipment = form.save()
            return redirect('equipment_update', equipment.id)

    else:
        form = EquipmentForm()

    return render(request,
                  'equipment/equipment_create.html',
                  {'form': form})


def network_create(request):
    if request.method == 'POST':
        form = NetworkForm(request.POST)

        if form.is_valid():
            network = form.save()
            return redirect('network_update', network.id)

    else:
        form = NetworkForm()

    return render(request,
                  'network/network_create.html',
                  {'form': form})

def place_equipment_create(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)

        if form.is_valid():
            place_equipment = form.save()
            return redirect('place_equipment_update', place_equipment.id)

    else:
        form = EquipmentForm()

    return render(request,
                  'place_equipment/place_equipment_create.html',
                  {'form': form})


def place_network_create(request):
    if request.method == 'POST':
        form = NetworkForm(request.POST)

        if form.is_valid():
            place_network = form.save()
            return redirect('place_network_update', place_network.id)

    else:
        form = NetworkForm()

    return render(request,
                  'place_network/place_network_create.html',
                  {'form': form})

def provider_create(request):
    if request.method == 'POST':
        form = ProviderForm(request.POST)

        if form.is_valid():
            provider = form.save()
            return redirect('provider_update', provider.id)

    else:
        form = ProviderForm()

    return render(request,
                  'provider/provider_create.html',
                  {'form': form})


def brand_create(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)

        if form.is_valid():
            brand = form.save()
            return redirect('brand_update', brand.id)

    else:
        form = BrandForm()

    return render(request,
                  'brand/brand_create.html',
                  {'form': form})


def typologie_update(request, id):
    typologie = get_object_or_404(Typologie, id=id)

    if request.method == 'POST':
        if 'delete' in request.POST:
            typologie.delete()
            messages.success(request, f'Le type d\'équipement "{typologie.name}" a été supprimé avec succès.')
            return redirect('typologie_list')
        else:
            form = TypologieForm(request.POST, instance=typologie)
            if form.is_valid():
                form.save()
                messages.success(request, f'Le type d\'équipement "{typologie.name}" a été mis à jour avec succès.')
                return redirect('typologie_update', id=typologie.id)
    else:
        form = TypologieForm(instance=typologie)

    return render(request, 'typologie/typologie_update.html', {'form': form, 'typologie': typologie})


def place_update(request, id):
    place = get_object_or_404(Place, id=id)

    if request.method == 'POST':
        if 'delete' in request.POST:
            place.delete()
            messages.success(request, f'Le type d\'équipement "{place.name}" a été supprimé avec succès.')
            return redirect('place_list')
        else:
            form = PlaceForm(request.POST, instance=place)
            if form.is_valid():
                form.save()
                messages.success(request, f'Le type d\'équipement "{place.name}" a été mis à jour avec succès.')
                return redirect('place_update', id=place.id)
    else:
        form = PlaceForm(instance=place)

    return render(request, 'place/place_update.html', {'form': form, 'place': place})

def type_connexion_update(request, id):
    type_connexion = get_object_or_404(Type_connexion, id=id)

    if request.method == 'POST':
        if 'delete' in request.POST:
            type_connexion.delete()
            messages.success(request, f'Le type d\'équipement "{type_connexion.name}" a été supprimé avec succès.')
            return redirect('type_connexion_list')
        else:
            form = Type_connexionForm(request.POST, instance=type_connexion)
            if form.is_valid():
                form.save()
                messages.success(request, f'Le type d\'équipement "{type_connexion.name}" a été mis à jour avec succès.')
                return redirect('type_connexion_update', id=type_connexion.id)
    else:
        form = Type_connexionForm(instance=type_connexion)

    return render(request, 'type_connexion/type_connexion_update.html', {'form': form, 'type_connexion': type_connexion})


def type_equipment_update(request, id):
    type_equipment = get_object_or_404(Type_equipment, id=id)

    if request.method == 'POST':
        if 'delete' in request.POST:
            type_equipment.delete()
            messages.success(request, f'Le type d\'équipement "{type_equipment.name}" a été supprimé avec succès.')
            return redirect('type_equipment_list')
        else:
            form = Type_equipmentForm(request.POST, instance=type_equipment)
            if form.is_valid():
                form.save()
                messages.success(request, f'Le type d\'équipement "{type_equipment.name}" a été mis à jour avec succès.')
                return redirect('type_equipment_update', id=type_equipment.id)
    else:
        form = Type_equipmentForm(instance=type_equipment)

    return render(request, 'type_equipment/type_equipment_update.html', {'form': form, 'type_equipment': type_equipment})



def equipment_update(request, id):
    equipment = get_object_or_404(Equipment, id=id)

    if request.method == 'POST':
        if 'delete' in request.POST:
            equipment.delete()
            messages.success(request, f'Le type d\'équipement a été supprimé avec succès.')
            return redirect('equipment_list')
        else:
            form = EquipmentForm(request.POST, instance=equipment)
            if form.is_valid():
                form.save()
                messages.success(request, f'Le type d\'équipement a été mis à jour avec succès.')
                return redirect('equipment_update', id=equipment.id)
    else:
        form = EquipmentForm(instance=equipment)

    return render(request, 'equipment/equipment_update.html', {'form': form, 'equipment': equipment})


def network_update(request, id):
    network = get_object_or_404(Network, id=id)

    if request.method == 'POST':
        if 'delete' in request.POST:
            network.delete()
            messages.success(request, f'Le type d\'équipement "{network.type_connection}" qui était à la "{network.rank}" place a été supprimé avec succès.')
            return redirect('network_list')
        else:
            form = NetworkForm(request.POST, instance=network)
            if form.is_valid():
                form.save()
                messages.success(request, f'Le type d\'équipement "{network.type_connection}" qui était à la "{network.rank}" a été mis à jour avec succès.')
                return redirect('network_update', id=network.id)
    else:
        form = NetworkForm(instance=network)

    return render(request, 'network/network_update.html', {'form': form, 'network': network})

def place_equipment_update(request, id):
    place_equipment = get_object_or_404(Equipment, id=id)

    if request.method == 'POST':
        if 'delete' in request.POST:
            place_equipment.delete()
            messages.success(request, f'Le type d\'équipement a été supprimé avec succès.')
            return redirect('place_equipment_list')
        else:
            form = EquipmentForm(request.POST, instance=place_equipment)
            if form.is_valid():
                form.save()
                messages.success(request, f'Le type d\'équipement a été mis à jour avec succès.')
                return redirect('place_equipment_update', id=place_equipment.id)
    else:
        form = EquipmentForm(instance=place_equipment)

    return render(request, 'place_equipment/place_equipment_update.html', {'form': form, 'place_equipment': place_equipment})


def place_network_update(request, id):
    place_network = get_object_or_404(Network, id=id)

    if request.method == 'POST':
        if 'delete' in request.POST:
            place_network.delete()
            messages.success(request, f'Le type d\'équipement "{place_network.type_connection}" qui était à la "{place_network.rank}" place a été supprimé avec succès.')
            return redirect('network_list')
        else:
            form = NetworkForm(request.POST, instance=place_network)
            if form.is_valid():
                form.save()
                messages.success(request, f'Le type d\'équipement "{place_network.type_connection}" qui était à la "{place_network.rank}" a été mis à jour avec succès.')
                return redirect('place_network_update', id=place_network.id)
    else:
        form = NetworkForm(instance=place_network)

    return render(request, 'place_network/place_network_update.html', {'form': form, 'place_network': place_network})


def provider_update(request, id):
    provider = get_object_or_404(Provider, id=id)

    if request.method == 'POST':
        if 'delete' in request.POST:
            provider.delete()
            messages.success(request, f'Le type d\'équipement "{provider.marque}" a été supprimé avec succès.')
            return redirect('provider_list')
        else:
            form = ProviderForm(request.POST, instance=provider)
            if form.is_valid():
                form.save()
                messages.success(request, f'Le type d\'équipement "{provider.marque}" a été mis à jour avec succès.')
                return redirect('provider_update', id=provider.id)
    else:
        form = ProviderForm(instance=provider)

    return render(request, 'provider/provider_update.html', {'form': form, 'provider': provider})


def brand_update(request, id):
    brand = get_object_or_404(Brand, id=id)

    if request.method == 'POST':
        if 'delete' in request.POST:
            brand.delete()
            messages.success(request, f'Le type d\'équipement "{brand.marque}" a été supprimé avec succès.')
            return redirect('brand_list')
        else:
            form =BrandForm(instance=brand)
            if form.is_valid():
                form.save()
                messages.success(request,
                                 f'Le type d\'équipement "{brand.marque}" a été mis à jour avec succès.')
                return redirect('brand_update', id=brand.id)
    else:
        form = BrandForm(instance=brand)

    return render(request, 'brand/brand_update.html',
                  {'form': form, 'brand': brand})

def typologie_delete(request, id):
    typologie = get_object_or_404(Typologie, id=id)

    if request.method == 'POST':
        typologie.delete()
        messages.success(request, f'La typologie "{typologie.name}" a été supprimé avec succès.')
        return redirect('typologie_list')

    return render(request, 'typologie/typologie_delete.html', {'typologie': typologie})


def place_delete(request, id):
    place = get_object_or_404(Place, id=id)

    if request.method == 'POST':
        place.delete()
        messages.success(request, f'Le site "{place.name}" a été supprimé avec succès.')
        return redirect('place_list')

    return render(request, 'place/place_delete.html', {'place': place})


def type_connexion_delete(request, id):
    type_connexion = get_object_or_404(Type_connexion, id=id)

    if request.method == 'POST':
        type_connexion.delete()
        messages.success(request, f'Le type de connexion "{type_connexion.name}" a été supprimé avec succès.')
        return redirect('type_connexion_list')

    return render(request, 'type_connexion/type_connexion_delete.html', {'type_connexion': type_connexion})


def type_equipment_delete(request, id):
    type_equipment = get_object_or_404(Type_equipment, id=id)

    if request.method == 'POST':
        type_equipment.delete()
        messages.success(request, f'Le type d équipement "{type_equipment.name}" a été supprimé avec succès.')
        return redirect('type_equipment_list')

    return render(request, 'type_equipment/type_equipment_delete.html', {'type_equipment': type_equipment})


def equipment_delete(request, id):
    equipment = get_object_or_404(Equipment, id=id)

    if request.method == 'POST':
        equipment.delete()
        messages.success(request, f'Le type d équipement "{equipment.type_equipment}" a été supprimé avec succès.')
        return redirect('equipment_list')

    return render(request, 'equipment/equipment_delete.html', {'equipment': equipment})


def network_delete(request, id):
    network = get_object_or_404(Network, id=id)

    if request.method == 'POST':
        network.delete()
        messages.success(request, f'Le type d équipement "{network.type_network}" a été supprimé avec succès.')
        return redirect('network_list')

    return render(request, 'network/network_delete.html', {'network': network})

def place_equipment_delete(request, id):
    place_equipment = get_object_or_404(Equipment, id=id)

    if request.method == 'POST':
        place_equipment.delete()
        messages.success(request, f'Le type d équipement "{place_equipment.type_equipment}" a été supprimé avec succès.')
        return redirect('place_equipment_list')

    return render(request, 'place_equipment/place_equipment_delete.html', {'place_equipment': place_equipment})


def place_network_delete(request, id):
    place_network = get_object_or_404(Network, id=id)

    if request.method == 'POST':
        place_network.delete()
        messages.success(request, f'Le type d équipement "{place_network.type_network}" a été supprimé avec succès.')
        return redirect('place_network_list')

    return render(request, 'place_network/place_network_delete.html', {'place_network': place_network})


def provider_delete(request, id):
    provider = get_object_or_404(Provider, id=id)

    if request.method == 'POST':
        provider.delete()
        messages.success(request, f'Le fournisseur "{provider.marque}" a été supprimé avec succès.')
        return redirect('provider_list')

    return render(request, 'provider/provider_delete.html', {'provider': provider})


def brand_delete(request, id):
    brand = get_object_or_404(Brand, id=id)

    if request.method == 'POST':
        brand.delete()
        messages.success(request, f'Le fournisseur "{brand.marque}" a été supprimé avec succès.')
        return redirect('brand_list')

    return render(request, 'brand/brand_delete.html', {'brand': brand})


def typologie(request):
    typologies = Typologie.objects.all()
    return render(request, 'typologie/typologie_list.html', {'typologies': typologies})


def place(request):
    places = Place.objects.all()
    return render(request, 'place/place_list.html', {'places': places})


def type_connexion(request):
    type_connexions = Type_connexion.objects.all()
    return render(request, 'type_connexion/type_connexion_list.html', {'type_connexions': type_connexions})


def type_equipment(request):
    type_equipments = Type_equipment.objects.all()
    return render(request, 'type_equipment/type_equipment_list.html', {'type_equipments': type_equipments})


def equipment(request):
    equipments = Equipment.objects.all()
    return render(request, 'equipment/equipment_list.html', {'equipments': equipments})


def network(request):
    networks = Network.objects.all()
    return render(request, 'network/network_list.html', {'networks': networks})

def place_equipment(request):
    place_equipments = Equipment.objects.all()
    return render(request, 'place_equipment/place_equipment_list.html', {'place_equipments': place_equipments})


def place_network(request):
    place_networks = Network.objects.all()
    return render(request, 'place_network/place_network_list.html', {'place_networks': place_networks})


def provider(request):
    providers = Provider.objects.all()
    return render(request, 'provider/provider_list.html', {'providers': providers})


def brand(request):
    brands = Brand.objects.all()
    return render(request, 'brand/brand_list.html', {'brands': brands})


def about(request):
    return render(request, 'autres/about.html')


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
                  'autres/contact.html',
                  {'form': form})


def email_sent(request):
    return render(request, 'autres/email_sent.html')