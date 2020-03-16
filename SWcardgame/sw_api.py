import requests
import json

cards = []

def get_characters(number):
    for n in range(1,number):
        response = requests.get(f'https://swapi.co/api/people/{n}')
        print(response)
        info = response.json()
        print(info)
        char_name = info['name']
        cards.append(char_name)
        print(cards)

def get_species(number):
    for number in range(1,31):
        response = requests.get(f'https://swapi.co/api/species/{number}')
        print(response)
        info = response.json()
        print(info)

def get_films(number):
    for number in range(1,8):
        response = requests.get(f'https://swapi.co/api/films/{number}')
        print(response)
        info = response.json()
        print(info)

get_characters(6)