import requests
import json

def get_characters(number):
    for number in range(1,30):
        response = requests.get(f'https://swapi.co/api/people/{number}')
        print(response)
        info = response.json()
        print(info)

def get_species(number):
    for number in range(1,30):
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

get_films(8)