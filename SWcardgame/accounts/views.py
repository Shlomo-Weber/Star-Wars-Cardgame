from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, logout as dlogout, login as dlogin
# Create your views here.

# def login(request):
#
#     return render(request, )

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
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            dlogin(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout(request):
    dlogout(request)
    return redirect('home')

