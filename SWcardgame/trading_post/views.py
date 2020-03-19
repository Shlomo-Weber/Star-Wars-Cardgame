from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from accounts.models import Profile
# Create your views here.


def card_collection(request):
    cards = Card.objects.all()

    return render(request, 'trading_post/card_collection.html', {'cards':cards})

def profile(request):
    prof = Profile.objects.all()

    return render(request, 'trading_post/profile.html', {'prof':prof})

