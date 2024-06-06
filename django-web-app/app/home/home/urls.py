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

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('email_sent/', views.email_sent, name='email_sent'),
]