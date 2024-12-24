import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '00d1b5e3f25a0bc4ff0fff159b323adf'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_create = {
    "name": "generate",
    "photo_id": -1
}
body_change = {
    "pokemon_id": "169671",
    "name": "New Name",
    "photo_id": -1
}
body_add_pokeball = {
    "pokemon_id": "169671"
}


'''response_create = requests.post(url = f'{URL}/pokemons',  headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_change = requests.put(url = f'{URL}/pokemons',  headers = HEADER, json = body_change)
print(response_change.text)'''

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball',  headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)

