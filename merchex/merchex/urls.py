# Un modèle d'URL, c’est la façon dont nous indiquons à Django qu'il doit être à l'écoute d'une requête pour une URL donnée, puis appeler une vue spécifique pour générer une page.
# Lorsque Django reçoit une requête HTTP, il tente de trouver une correspondance pour le chemin de cette requête dans une liste de modèles d'URL, définis dans urls.py.

from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('listings/', views.listings),
    path('contact-us/', views.contact),
    path('about-us/', views.about),
]
