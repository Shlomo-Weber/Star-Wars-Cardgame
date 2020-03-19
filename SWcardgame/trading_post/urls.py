from django.contrib import admin
from django.urls import path, include
from trading_post.views import *

urlpatterns = [
    path('card_collection/', card_collection, name='card_collection' ),
    path('profile/', profile, name = 'profile')
]