import random
import json
from entities import Pokemon
from buildDB import buildPokedex
import views

with open('pokedex.json', 'r') as file:
    pokedex = json.load(file)
if len(pokedex) == 0:
    buildPokedex()

def createPokemonObject(pokemonID, data):
    return Pokemon(
        pokemonID,
        data["name"],
        data["types"],
        data["base_stats"],
        data["allMoves"]
    )

def pokemonSelect():
    pokemonNames = [data["name"] for data in pokedex.values()]
    choices = random.sample(pokemonNames, 10)
    views.showPokemonChoices(choices)
    team = []
    while len(team) < 3:
        chosen = views.getPokemonChoice(team)
        if chosen.isnumeric():
            index = int(chosen) - 1
            if 0 <= index < len(choices):
                chosen = choices[index]
        if chosen not in choices:
            views.showInvalidChoice()
            continue
        if any(p.name == chosen for p in team):
            views.typewriter("Already selected!")
            continue
        for pokemonID, data in pokedex.items():
            if data["name"] == chosen:
                pokemon = createPokemonObject(pokemonID, data)
                team.append(pokemon)
                views.typewriter(f"{pokemon.name} joined the team!")
                break
    return team

def opponentPokemonSelect():
    pokemonNames = [data["name"] for data in pokedex.values()]
    opponentTeamNames = random.sample(pokemonNames, 3)
    opponentTeam = []
    for pokemonID, data in pokedex.items():
        if data["name"] in opponentTeamNames:
            pokemon = createPokemonObject(pokemonID, data)
            opponentTeam.append(pokemon)
    views.typewriter(f"Your opponent's team is {opponentTeam}")
    return opponentTeam


views.introGame()
pokemonSelect()
opponentPokemonSelect()
