import requests

url = "https://pokeapi.co/api/v2/pokemon?limit=151"

response =requests.get(url)


for pokemon in response.json()["results"]:
    print(pokemon["name"])


