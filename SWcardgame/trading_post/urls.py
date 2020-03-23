from django.contrib import admin
from django.urls import path, include
from trading_post.views import *

urlpatterns = [
    path('card_collection/', card_collection, name='card_collection' ),
    path('profile/', profile, name = 'profile'),
    path('start_game/', start_game, name = 'start_game'),
    path('switch_card/<int:card_id>', switch_card, name = 'switch_card'),
    path('make_offer/<int:trade_id>', make_offer, name='make_offer'),
    path('start_trade/<int:card_id>', initiate_trade, name='start_trade'),
    path('all_trades/', show_trades, name='all_trades'),
    path('delete_trade/<int:trade_id>', delete_trade, name='delete_trade'),
    path('my_trades/', my_trades, name='my_trades'),
    path('handle_offer/<int:offer_id>/<int:status>', handle_offer, name='handle_offer')
]

