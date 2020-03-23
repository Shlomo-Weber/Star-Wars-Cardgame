from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from accounts.models import Profile
import random
from django.db.models import Sum, Count
from django.contrib import messages
from .forms import *
# Create your views here.


def card_collection(request):
    cards = Card.objects.all()
    return render(request, 'trading_post/card_collection.html', {'cards':cards})


def start_game(request):
    game = Game(initiator=request.user.profile)
    game.save()
    deck = request.user.profile.deck
    while len(deck.hand.all()) != 5:
        crd = random.choice(deck.cards.all())
        if crd not in deck.hand.all():
            deck.hand.add(crd)
    hand = request.user.profile.deck.hand.all()
    total_points = 0
    for card in hand:
        total_points += card.films.all().count()
    return render(request, 'trading_post/start_game.html', {'points':total_points})


def profile(request):
    return render(request,'trading_post/profile.html',)


def switch_card(request, card_id):
    deck = request.user.profile.deck
    if deck.mulligans < 2:
        available_cards = deck.cards.all().difference(deck.hand.all())
        selected_card = random.choice(available_cards)
        old_card = Card.objects.get(id=card_id)
        deck.hand.remove(old_card)
        deck.hand.add(selected_card)
        deck.mulligans += 1
        deck.save()
    else:
        messages.error(request, 'MULLIGAN LIMIT EXCEEDED!')
    return redirect('start_game')


def initiate_trade(request, card_id):
    card = Card.objects.get(id=card_id)
    trade, created = Trade.objects.get_or_create(card= card, profile = request.user.profile)
    return redirect('show_trades')#TODO write url


def show_trades(request):
    trades = Trade.objects.all()
    return render(request, 'trading_post/all_trades.html', {'trades':trades})#TODO write url


def make_offer(request, trade_id):
    trade = Trade.objects.get(id=trade_id)
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit = False)
            offer.trade = trade
            offer.profile = request.user.profile
            offer.save()
            return redirect('show_trades')
        messages.error(request, 'FORM ERROR')
    form = OfferForm()
    form.fields['card'].queryset = request.user.profile.deck.cards.all()
    return render(request, 'trading_post/make_offer.html',{'form':form})#TODO write url


