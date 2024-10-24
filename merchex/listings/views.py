# Une vue a pour fonction de répondre à la visite d'un utilisateur sur le site en renvoyant une page que l’utilisateur peut voir.
# Une vue est une fonction qui accepte un objet HttpRequest comme paramètre et retourne un objet HttpResponse.

from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing
from django.shortcuts import render

def hello(request):
    bands = Band.objects.all()
    return render(request,
    'listings/hello.html',
    {'bands': bands})

def listings(request):
    listings = Listing.objects.all()
    return render(request,
    'listings/listings.html',
    {'listings': listings})

def about(request):
    return HttpResponse('<h1>About us. We love merchandising.</h1>')

def contact(request):
    return HttpResponse('<h1>Contact us. Right now.</h1>')