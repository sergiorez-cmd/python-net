#!/usr/bin/env python3
# Programação de redes com python3
# https://requests.readthedocs.io/en/latest/
# Obter coordenadas de um endereço via HTTP requests

import requests

add_street = input ('Digite Número, Rua, Cidade, Estado:')

def geocode(address):
    base = 'https://nominatim.openstreetmap.org/search'
    parameters = {'q': address, 'format': 'json'}
    user_agent = 'Geocode Location'
    headers = {'User-Agent': user_agent}
    response = requests.get(base, params=parameters, headers=headers)
    reply = response.json()
    print (reply[0]['lat'], reply[0]['lon'])

if __name__ == '__main__':
    geocode(add_street)

