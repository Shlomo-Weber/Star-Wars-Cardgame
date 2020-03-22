from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from accounts.models import Profile
import random
# Create your views here.


def card_collection(request):
    cards = Card.objects.all()
    return render(request, 'trading_post/card_collection.html', {'cards':cards})


def start_game(request):
    deck = Deck(user=request.user)
    deck.save()
    for number in range(15):
        card = random.choice(Card.objects.all())
        deck.cards.add(card)
    game = Game(initiator=request.user.profile, initiator_deck=deck)
    game.save()
    while len(deck.hand.all()) != 5:
        crd = random.choice(deck.cards.all())
        if crd not in deck.hand.all():
            deck.hand.add(crd)
    return render(request, 'trading_post/start_game.html', {'cards':deck.hand.all()})


def profile(request):
    return render(request, 'trading_post/profile.html', )
