from django.shortcuts import render

from .models import Offer

def allOffers(request):
    offerList = Offer.objects.all()
    context = {'offerList': offerList}
    return render(request, 'offerStream/allOffers.html', context)
