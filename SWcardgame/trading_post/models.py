from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Card(models.Model):
    title = models.CharField(max_length=60)
    species = models.ForeignKey('Species', on_delete=models.CASCADE, null=True)
    films = models.ManyToManyField('Film')
    deck = models.ForeignKey('Deck', on_delete=models.CASCADE, null=True)


class Species(models.Model):
    name = models.CharField(max_length=100)


class Film(models.Model):
    title = models.CharField(max_length=60)


class Deck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
