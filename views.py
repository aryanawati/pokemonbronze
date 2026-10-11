import time
import sys
from entities import Pokemon
import json
import random

with open('pokedex.json', 'r') as file:
    pokedex = json.load(file)

def typewriter(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print() # Add a newline at the end
    time.sleep(0.3) # Brief pause after a sentence

def introGame():
    typewriter("Welcome to Pokemon Bronze!")

def showPokemonChoices(choices):
    typewriter("Choose 3 Pokemon for your team!")
    for i, name in enumerate(choices, 1):
        typewriter(f"{i}. {name}", speed=0.01)

def getPokemonChoice(team):
    typewriter(f"Current Team: {team}")
    typewriter(f"Choose {3 - len(team)} more Pokemon!")
    return input("I choose: ").title()

def showInvalidChoice():
    typewriter("Choose one from the list...")
