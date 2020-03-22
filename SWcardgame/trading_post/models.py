from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile
# Create your models here.

class Card(models.Model):
    title = models.CharField(max_length=60)
    species = models.ForeignKey('Species', on_delete=models.CASCADE, null=True)
    films = models.ManyToManyField('Film')

    def __str__(self):
        return self.title


class Species(models.Model):
    name = models.CharField(max_length=100)


class Film(models.Model):
    title = models.CharField(max_length=60)


class Deck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cards = models.ManyToManyField(Card, related_name = "deck_cards")
    hand = models.ManyToManyField(Card, related_name = "deck_hand_cards")

class Game(models.Model):
    initiator = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name ='initiator')
    other_player = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name = 'other_player', null = True)
    initiator_deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name = 'initiator_deck')
    other_deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name = 'other_deck', null = True)

