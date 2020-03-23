from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile
# Create your models here.

STATUS_CHOICES = {
    ('A', 'Accepted'),
    ('R', 'Rejected'),
    ('P', 'Pending'),
}

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
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    cards = models.ManyToManyField(Card, related_name = "deck_cards")
    hand = models.ManyToManyField(Card, related_name = "deck_hand_cards")
    mulligans = models.IntegerField(default=0)


class Game(models.Model):
    initiator = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name ='initiator')
    other_player = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name = 'other_player', null = True)

class Trade(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, default='P', max_length=10)


class Offer(models.Model):
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, default='P', max_length = 10)
