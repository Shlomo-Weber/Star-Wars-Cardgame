from django.shortcuts import render, redirect, get_object_or_404
from .models import *
# Create your views here.


def card_collection(request):
    cards = Card.objects.all()

    return render(request, 'trading_post/card_collection.html', {'cards':cards})

