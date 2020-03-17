from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.forum_page, name='Forum'),
    path('post/<int:post_id>', views.show_post, name='show_post'),

]