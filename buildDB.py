import requests
import json
import time

def buildPokedex():
    pokedex = {}
    for i in range(1,152):
        strID = f"{i:03d}" #Format the ID into 3 digit format

        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}")
        data = response.json()

        pokedex[strID] = {
                    "name": data["name"].capitalize(),
                    "types": [t["type"]["name"].capitalize() for t in data["types"]],
                    "base_exp": data["base_experience"],
                    "base_stats": {
                        "hp": data["stats"][0]["base_stat"],
                        "attack": data["stats"][1]["base_stat"],
                        "defense": data["stats"][2]["base_stat"],
                        "speed": data["stats"][5]["base_stat"]
                    },
                    "allMoves": [move["move"]["name"].replace("-", " ").title() for move in data["moves"]],
                }
    

    with open('pokedex.json', 'w') as file:
            json.dump(pokedex, file, indent=4)

    return pokedex

if __name__ == "__main__":
    buildPokedex()