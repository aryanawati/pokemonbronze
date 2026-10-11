import random
import json

with open('pokedex.json', 'r') as file:
    pokedex = json.load(file)

class Pokemon:
    def __init__(self, id, name, types, stats, moves):
        self.name = name
        self.id = id
        self.type = types
        self.level = 50
        self.baseatk = stats["attack"]
        self.basedef = stats["defense"]
        self.basehp = stats["hp"]
        self.basespd = stats['speed']
        self.moves = moves

    def __repr__(self):
        return f"'{self.name}'"

    def selectablePokemon(self):
        allPokemon = pokedex[self.id]["names"]
        choosePokemon = random.sample(allPokemon, 10)
        return choosePokemon

    def selectableMoves(self):
        allMoves = pokedex[self.id]["allMoves"]
        sampleSize = min(10, len(allMoves))
        chooseMoves = random.sample(allMoves, sampleSize)
        return chooseMoves

class Move:
    def __init__(self, moveName, pokemon, baseDamage, type, isAttack):
        self.moveName = moveName
        self.pokemon = pokemon
        self.baseDamage = baseDamage
        self.type = type
        self.isAttack = isAttack

