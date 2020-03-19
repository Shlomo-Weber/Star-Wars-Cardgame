import requests
import json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SWcardgame.settings')
import django
django.setup()
from trading_post.models import *
import random
from accounts.models import Type

def add_types():
    type_choices = ['Jedi','Sith','Hutt','Bounty Hunter','Tusken Raider', 'Droid']
    for type in type_choices:
        t = Type(name = type)
        print('adding types')
        t.save()


def get_characters(number):
    n=1
    while Card.objects.all().count() < number:
        print(f'Creating character {n}/{number}')
        response = requests.get(f'https://swapi.co/api/people/{n}')
        n += 1
        print(response)
        if response.status_code == 404:
            continue
        response=response.json()
        for i in response['species'][0].split('/'):
            if i.isdigit():
                species = Species.objects.get(id=i)
        print(response['name'])
        if not species:
            species = Species.objects.get(id=random.choice([1,2,3,4,5]))
        card, created = Card.objects.get_or_create(title=response['name'], species=species)
        card.save()

def get_species():
    response = requests.get('https://swapi.co/api/species/')
    response = response.json()
    for n in range(1, response['count'] + 1):
        print(f'Creating species {n}')
        response = requests.get(f'https://swapi.co/api/species/{n}')
        response = response.json()
        print(response['name'])
        species = Species(name=response['name'])
        species.save()


def get_films(number):
    for number in range(1,8):
        response = requests.get(f'https://swapi.co/api/films/{n}')
        print(response)
        info = response.json()
        print(info)

if Species.objects.all().count()<5:
    get_species()


# get_characters(30)
add_types()
