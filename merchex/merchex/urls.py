# Un modèle d'URL, c’est la façon dont nous indiquons à Django qu'il doit être à l'écoute d'une requête pour une URL donnée, puis appeler une vue spécifique pour générer une page.
# Lorsque Django reçoit une requête HTTP, il tente de trouver une correspondance pour le chemin de cette requête dans une liste de modèles d'URL, définis dans urls.py.

from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    # ADMIN
    path('admin/', admin.site.urls, name='admin'),
    # HOMEPAGE
    path('', views.home, name='home'),
    # BAND
    path('bands/', views.band_list, name='band-list'),
    path('bands/<int:id>/', views.band_detail, name='band-detail'),
    path('bands/add/', views.band_create, name='band-create'),
    path('bands/<int:id>/change/', views.band_update, name='band-update'),
    path('bands/<int:id>/delete/', views.band_delete, name='band-delete'),
    # LISTING
    path('listings/', views.listing_list, name='listing-list'),
    path('listings/<int:id>/', views.listing_detail, name='listing-detail'),
    path('listings/add/', views.listing_create, name='listing-create'),
    path('listings/<int:id>/change/', views.listing_update, name='listing-update'),
    path('listings/<int:id>/delete/', views.listing_delete, name='listing-delete'),
    # ABOUT
    path('about-us/', views.about, name='about-us'),
    # CONTACT
    path('contact-us/', views.contact, name='contact-us'),
]
