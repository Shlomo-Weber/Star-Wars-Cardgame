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