from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('accueil/', views.accueil, name='accueil'),
    path('entreprise/', views.entreprise, name='entreprise'),
    path('equipement/', views.equipement, name='equipement'),
    path('reseau/', views.reseau, name='reseau'),
    path('logiciel/', views.logiciel, name='logiciel'),
    path('contact/', views.accueil, name='contact'),
    path('about/', views.about, name='about'),

    path('admin/', admin.site.urls),
    path('bands/', views.band_list, name='band-list'),
    path('bands/<int:id>/', views.band_detail, name='band-detail'),
    path('bands/add/', views.band_create, name='band-create'),
    path('bands/<int:id>/change/', views.band_update, name='band-update'),
    path('listings/add/', views.listing_create, name='listing-create'),
    path('listings/<int:id>/change/', views.listing_update, name='listing-update'),  # Nouveau chemin pour mettre à jour une annonce
    path('contact-us/', views.contact, name='contact'),
    path('listings/<int:id>/', views.listing_detail, name='listing-detail'),
    path('listings/', views.listing_list, name='listing-list'),
    path('about/', views.about, name='about'),
    path('email-sent/', views.email_sent, name='email-sent'),
    path('bands/<int:id>/delete/', views.band_delete, name='band-delete'),
    path('listings/<int:id>/delete/', views.listing_delete, name='listing_delete'),
]
