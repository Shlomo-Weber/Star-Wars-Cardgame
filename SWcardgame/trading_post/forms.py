from django import forms
from django.forms import ModelForm
from .models import *


class OfferForm(ModelForm):
    class Meta:
        model = Offer
        fields = ['card']

