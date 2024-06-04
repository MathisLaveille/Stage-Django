from django.contrib import admin
from django.urls import path
from listings import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.about, name='about'),

    # path('bands/', views.band_list, name='band_list'),
    path('bands/', views.band_list2.as_view(), name='band_list'),
    path('bands/add/', views.band_create, name='band_create'),
    path('bands/<int:id>/', views.band_detail, name='band_detail'),
    path('bands/<int:id>/change/', views.band_update, name='band_update'),
    path('bands/<int:id>/delete/', views.band_delete, name='band_delete'),

    # path('listings/', views.listing_list, name='listing_list'),
    path('listings/', views.listing_list2.as_view(), name='listing_list'),
    path('listings/add/', views.listing_create, name='listing_create'),
    path('listings/<int:id>/', views.listing_detail, name='listing_detail'),
    path('listings/<int:id>/change/', views.listing_update, name='listing_update'),
    path('listings/<int:id>/delete/', views.listing_delete, name='listing_delete'),


    path('about/', views.about, name='about'),
    path('contact_us/', views.contact, name='contact'),
    path('email_sent/', views.email_sent, name='email_sent'),
]
