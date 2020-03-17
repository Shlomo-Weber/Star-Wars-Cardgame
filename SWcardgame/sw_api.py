import requests
import json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SWcardgame.settings')
import django

django.setup()
from trading_post.models import *

def get_characters(number):
    for n in range(1,number):
        char_response = requests.get(f'https://swapi.co/api/people/{n}')
        print(char_response)
        char_response=char_response.json()
        for i in char_response['species'.split('/')]:
            if i.isdigit():
                species = Species.objects.get(id=i)
        print(char_response['name'])
        if not species:
            species = Species.objects.get(id=1)
        card = Card(title=char_response['name'], species = species, )

def get_species():
    response = requests.get('https://swapi.co/api/species/')
    for n in range(1, response['count']):
        response = requests.get(f'https://swapi.co/api/species/{n}')
        for i in response['species'].split('/'):
            species = Species.objects.get(id=i)
            print(response)
            if not species:
                species = Species.objects.get(id=1)
        # species = Species(name = response['name'])



def get_films(number):
    for number in range(1,8):
        response = requests.get(f'https://swapi.co/api/films/{n}')
        print(response)
        info = response.json()
        print(info)

get_characters(4)