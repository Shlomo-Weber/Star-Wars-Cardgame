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
    return redirect('all_trades')


def show_trades(request):
    trades = Trade.objects.all()
    return render(request, 'trading_post/all_trades.html', {'trades':trades})


def make_offer(request, trade_id):
    trade = Trade.objects.get(id=trade_id)
    if request.user.profile == trade.profile:
        messages.error(request, "CAN'T MAKE OFFER ON OWN TRADE!")
        return redirect('all_trades')
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit = False)
            offer.trade = trade
            offer.profile = request.user.profile
            offer.save()
            return redirect('all_trades')
        messages.error(request, 'FORM ERROR')
    form = OfferForm()
    form.fields['card'].queryset = request.user.profile.deck.cards.all()
    return render(request, 'trading_post/make_offer.html',{'form':form})


def delete_trade(request, trade_id):
    trade = Trade.objects.get(id=trade_id)
    if request.user.profile != trade.profile:
        messages.error(request, "CAN ONLY DELETE YOUR OWN TRADES!")
        return redirect('all_trades')
    trade.delete()
    messages.success(request, 'TRADE REMOVED SUCCESSFULLY')
    return redirect('all_trades')

def my_trades(request):
    trades = request.user.profile.trade_set.all().exclude(status='A')
    return render(request, 'trading_post/show_offers.html', {'trades':trades})


def handle_offer(request, offer_id, status):
    offer = Offer.objects.get(id=offer_id)
    if status == 1:
        offer.status = 'A'

        trade_card = offer.trade.card
        offer_card = offer.card
        #managing original trade makers cards
        offer.trade.profile.deck.cards.remove(trade_card)
        offer.trade.profile.deck.cards.add(offer_card)
        if trade_card in offer.trade.profile.deck.hand.all():
            offer.trade.profile.deck.hand.remove(trade_card)
            offer.trade.profile.deck.hand.add(offer_card)

        #managing offer makers cards
        offer.profile.deck.cards.remove(offer_card)
        offer.profile.deck.cards.add(trade_card)
        if trade_card in offer.profile.deck.hand.all():
            offer.profile.deck.hand.remove(offer_card)
            offer.profile.deck.hand.add(trade_card)

        #setting all other offers to rejected
        for offer1 in offer.trade.offer_set.all():
            if offer1 != offer:
                offer1.status = 'R'
                offer1.save()
        trade = offer.trade
        trade.status = 'A'
        trade.save()
    else:
        offer.status = 'R'
    offer.save()
    return redirect('my_trades')




