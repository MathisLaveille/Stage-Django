from django.contrib import admin
from django.urls import path
from appinfra import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accueil, name='accueil'),

    path('typologie/', views.typologie_list.as_view(), name='typologie_list'),
    path('typologie/add/', views.typologie_create, name='typologie_create'),
    path('typologie/<int:id>/', views.typologie_detail, name='typologie_detail'),
    path('typologie/<int:id>/change/', views.typologie_update, name='typologie_update'),
    path('typologie/<int:id>/delete/', views.typologie_delete, name='typologie_delete'),

    path('place/', views.place_list.as_view(), name='place_list'),
    path('place/add/', views.place_create, name='place_create'),
    path('place/<int:id>/', views.place_detail, name='place_detail'),
    path('place/<int:id>/change/', views.place_update, name='place_update'),
    path('place/<int:id>/delete/', views.place_delete, name='place_delete'),

    path('type_connexion/', views.type_connexion_list.as_view(), name='type_connexion_list'),
    path('type_connexion/add/', views.type_connexion_create, name='type_connexion_create'),
    path('type_connexion/<int:id>/', views.type_connexion_detail, name='type_connexion_detail'),
    path('type_connexion/<int:id>/change/', views.type_connexion_update, name='type_connexion_update'),
    path('type_connexion/<int:id>/delete/', views.type_connexion_delete, name='type_connexion_delete'),

    path('provider/', views.provider_list.as_view(), name='provider_list'),
    path('provider/add/', views.provider_create, name='provider_create'),
    path('provider/<int:id>/', views.provider_detail, name='provider_detail'),
    path('provider/<int:id>/change/', views.provider_update, name='provider_update'),
    path('provider/<int:id>/delete/', views.provider_delete, name='provider_delete'),

    path('brand/', views.brand_list.as_view(), name='brand_list'),
    path('brand/add/', views.brand_create, name='brand_create'),
    path('brand/<int:id>/', views.brand_detail, name='brand_detail'),
    path('brand/<int:id>/change/', views.brand_update, name='brand_update'),
    path('brand/<int:id>/delete/', views.brand_delete, name='brand_delete'),

    path('type_equipment/', views.type_equipment_list.as_view(), name='type_equipment_list'),
    path('type_equipment/add/', views.type_equipment_create, name='type_equipment_create'),
    path('type_equipment/<int:id>/', views.type_equipment_detail, name='type_equipment_detail'),
    path('type_equipment/<int:id>/change/', views.type_equipment_update, name='type_equipment_update'),
    path('type_equipment/<int:id>/delete/', views.type_equipment_delete, name='type_equipment_delete'),

    path('equipment/', views.equipment_list.as_view(), name='equipment_list'),
    path('equipment/add/', views.equipment_create, name='equipment_create'),
    path('equipment/<int:id>/', views.equipment_detail, name='equipment_detail'),
    path('equipment/<int:id>/change/', views.equipment_update, name='equipment_update'),
    path('equipment/<int:id>/delete/', views.equipment_delete, name='equipment_delete'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('email_sent/', views.email_sent, name='email_sent'),
]