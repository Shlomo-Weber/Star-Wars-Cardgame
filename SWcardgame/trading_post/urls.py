from django.contrib import admin
from django.urls import path, include
from trading_post.views import *

urlpatterns = [
    path('card_collection/', card_collection, name='card_collection' ),
    path('profile/', profile, name = 'profile'),
    path('start_game/', start_game, name = 'start_game'),
    path('switch_card/<int:card_id>', switch_card, name = 'switch_card'),
    path('show_trades/', show_trades, name='show_trades'),
    path('make_offer/<int:trade_id>', make_offer, name='make_offer'),
    path('start_trade/<int:card_id>', initiate_trade, name='start_trade')
]

