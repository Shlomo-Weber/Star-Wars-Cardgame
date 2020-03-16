from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup,name = 'signup'),
    path('login/', login, name = 'login'),
    path('logout/', logout, name='logout'),
    # path('profile/<int:user_pk>', profile, name='profile')
    ]