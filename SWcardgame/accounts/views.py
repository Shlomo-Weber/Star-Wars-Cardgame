from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, logout as dlogout, login as dlogin
from .models import Profile
from trading_post.models import Deck, Card
import random

# Create your views here.
def home(request):
    return render(request, 'accounts/homepage.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                messages.warning(request, f'{form.cleaned_data["username"]} is already in use')
                return redirect('signup')
            user = User.objects.create_user(**form.cleaned_data)
        return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login(request):
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            dlogin(request, user)
            if Profile.objects.filter(user=user).exists():
                deck = request.user.profile.deck
                deck.mulligans = 0
                deck.save()
                for number in range(15):
                    card = random.choice(Card.objects.all())
                    deck.cards.add(card)
                return redirect('profile')
            return redirect('create_profile')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form':form})


def logout(request):
    dlogout(request)
    return redirect('home')


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            profile_f = form.save(commit=False)
            profile_f.user = request.user
            profile_f.save()
            deck = Deck(profile=request.user.profile)
            deck.save()
            for number in range(15):
                card = random.choice(Card.objects.all())
                deck.cards.add(card)
            return redirect('profile')
        messages.warning(request, 'This is not a valid form')
        return redirect('create_profile')
    else:
        form = ProfileForm()
        return render(request, 'accounts/create_profile.html', {'form':form})