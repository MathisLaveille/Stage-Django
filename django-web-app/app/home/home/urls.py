from django.contrib import admin
from django.urls import path
from django.utils.translation import gettext as _
from appinfra import views, models, forms, tables

urlpatterns = [
    # _____________________________________________BASE_________________________________________________________________

    path('admin/', admin.site.urls),
    path('', views.accueil, name='accueil'),

    # _____________________________________________TYPOLOGIE____________________________________________________________

    path('typologie/', views.MyTemplateView.as_view(
        model=models.Typologie,
        template_name='typologie/typologie_list.html',
        class_table=tables.TypologieTable,
    ), name='typologie_list'),

    path('typologie/add/', views.MyTemplateView.as_view(
        model=models.Typologie,
        template_name='typologie/typologie_create.html',
        class_form=forms.TypologieForm,
        action="new"
    ), name='typologie_create'),

    path('typologie/<int:id>/change/', views.MyTemplateView.as_view(
        model=models.Typologie,
        template_name="typologie/typologie_update.html",
        class_form=forms.TypologieForm
    ), name='typologie_update', kwargs={'title': _("typologie")}),

    # _____________________________________________PLACE________________________________________________________________

    path('place/', views.MyTemplateView.as_view(
        model=models.Place,
        template_name='place/place_list.html',
        class_table=tables.PlaceTable,
    ), name='place_list'),

    path('place/add/', views.MyTemplateView.as_view(
        model=models.Place,
        template_name='place/place_create.html',
        class_form=forms.PlaceForm,
        action="new"
    ), name='place_create'),

    path('place/<int:id>/equipments/', views.MyTemplateView.as_view(
        model=models.Equipment,
        template_name='equipment/equipment_list.html',
        class_table=tables.EquipmentTable,
        source=models.Place
    ), name='place_equipments'),

    path('place/<int:id>/networks/', views.MyTemplateView.as_view(
        model=models.Network,
        template_name='network/network_list.html',
        class_table=tables.NetworkTable,
        source=models.Place
    ), name='place_networks'),

    path('place/<int:id>/softwares/', views.MyTemplateView.as_view(
        model=models.Software,
        template_name='software/software_list.html',
        class_table=tables.SoftwareTable,
        source=models.Place
    ), name='place_softwares'),

    path('place/<int:id>/change/', views.MyTemplateView.as_view(
        model=models.Place,
        template_name="place/place_update.html",
        class_form=forms.PlaceForm
    ), name='place_update', kwargs={'title': _("Place")}),

    # _____________________________________________TYPE-CONNEXION_______________________________________________________

    path('type_connexion/', views.MyTemplateView.as_view(
        model=models.Type_connexion,
        template_name='type_connexion/type_connexion_list.html',
        class_table=tables.Type_connexionTable,
    ), name='type_connexion_list'),

    path('type_connexion/add/', views.MyTemplateView.as_view(
        model=models.Type_connexion,
        template_name='type_connexion/type_connexion_create.html',
        class_form=forms.Type_connexionForm,
        action = "new"
    ), name='type_connexion_create'),

    path('type_connexion/<int:id>/change/', views.MyTemplateView.as_view(
        model=models.Type_connexion,
        template_name="type_connexion/type_connexion_update.html",
        class_form=forms.Type_connexionForm
    ), name='type_connexion_update', kwargs={'title': _("type_connexion")}),

    # _____________________________________________PROVIDER_____________________________________________________________

    path('provider/', views.MyTemplateView.as_view(
        model=models.Provider,
        template_name='provider/provider_list.html',
        class_table=tables.ProviderTable,
    ), name='provider_list'),

    path('provider/add/', views.MyTemplateView.as_view(
        model=models.Provider,
        template_name='provider/provider_create.html',
        class_form=forms.ProviderForm,
        action = "new"
    ), name='provider_create'),

    path('provider/<int:id>/change/', views.MyTemplateView.as_view(
        model=models.Provider,
        template_name="provider/provider_update.html",
        class_form=forms.ProviderForm
    ), name='provider_update', kwargs={'title': _("provider")}),

    # _____________________________________________BRAND________________________________________________________________

    path('brand/', views.MyTemplateView.as_view(
        model=models.Brand,
        template_name='brand/brand_list.html',
        class_table=tables.BrandTable,
    ), name='brand_list'),

    path('brand/add/', views.MyTemplateView.as_view(
        model=models.Brand,
        template_name='brand/brand_create.html',
        class_form=forms.BrandForm,
        action = "new"
    ), name='brand_create'),

    path('brand/<int:id>/change/', views.MyTemplateView.as_view(
        model=models.Brand,
        template_name="brand/brand_update.html",
        class_form=forms.BrandForm
    ), name='brand_update', kwargs={'title': _("brand")}),

    # _____________________________________________TYPE-EQUIPMENT_______________________________________________________

    path('type_equipment/', views.MyTemplateView.as_view(
        model=models.Type_equipment,
        template_name='type_equipment/type_equipment_list.html',
        class_table=tables.Type_equipmentTable,
    ), name='type_equipment_list'),

    path('type_equipment/add/', views.MyTemplateView.as_view(
        model=models.Type_equipment,
        template_name='type_equipment/type_equipment_create.html',
        class_form=forms.Type_equipmentForm,
        action = "new"
    ), name='type_equipment_create'),

    path('type_equipment/<int:id>/change/', views.MyTemplateView.as_view(
        model=models.Type_equipment,
        template_name="type_equipment/type_equipment_update.html",
        class_form=forms.Type_equipmentForm
    ), name='type_equipment_update', kwargs={'title': _("type_equipment")}),

    # _____________________________________________PLATFORM_____________________________________________________________

    path('platform/', views.MyTemplateView.as_view(
        model=models.Platform,
        template_name='platform/platform_list.html',
        class_table=tables.PlatformTable,
    ), name='platform_list'),

    path('platform/add/', views.MyTemplateView.as_view(
        model=models.Platform,
        template_name='platform/platform_create.html',
        class_form=forms.PlatformForm,
        action="new"
    ), name='platform_create'),

    path('platform/<int:id>/change/', views.MyTemplateView.as_view(
        model=models.Platform,
        template_name="platform/platform_update.html",
        class_form=forms.PlatformForm
    ), name='platform_update', kwargs={'title': _("platform")}),

    # _____________________________________________EQUIPMENT____________________________________________________________

    path('equipment/', views.MyTemplateView.as_view(
        model=models.Equipment,
        template_name='equipment/equipment_list.html',
        class_table=tables.EquipmentTable,
    ), name='equipment_list'),

    path('equipment/add/', views.MyTemplateView.as_view(
        model=models.Equipment,
        template_name='equipment/equipment_create.html',
        class_form=forms.EquipmentForm,
        action="new"
    ), name='equipment_create'),

    path('equipment/<int:id>/change/', views.MyTemplateView.as_view(
        model=models.Equipment,
        template_name="equipment/equipment_update.html",
        class_form=forms.EquipmentForm
    ), name='equipment_update', kwargs={'title': _("equipment")}),

    # _____________________________________________NETWORK______________________________________________________________

    path('network/', views.MyTemplateView.as_view(
        model=models.Network,
        template_name='network/network_list.html',
        class_table=tables.NetworkTable,
    ), name='network_list'),

    path('network/add/', views.MyTemplateView.as_view(
        model=models.Network,
        template_name='network/network_create.html',
        class_form=forms.NetworkForm,
        action="new"
    ), name='network_create'),

    path('network/<int:id>/change/', views.MyTemplateView.as_view(
        model=models.Network,
        template_name="network/network_update.html",
        class_form=forms.NetworkForm
    ), name='network_update', kwargs={'title': _("network")}),

    # _____________________________________________SOFTWARE_____________________________________________________________

    path('software/', views.MyTemplateView.as_view(
        model=models.Software,
        template_name='software/software_list.html',
        class_table=tables.SoftwareTable,
    ), name='software_list'),

    path('software/add/', views.MyTemplateView.as_view(
        model=models.Software,
        template_name='software/software_create.html',
        class_form=forms.SoftwareForm,
        action="new"
    ), name='software_create'),

    path('software/<int:id>/change/', views.MyTemplateView.as_view(
        model=models.Software,
        template_name="software/software_update.html",
        class_form=forms.SoftwareForm
    ), name='software_update', kwargs={'title': _("software")}),

    # _____________________________________________MORE_________________________________________________________________

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('email_sent/', views.email_sent, name='email_sent'),
]
