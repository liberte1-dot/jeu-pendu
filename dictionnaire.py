import random

mots = [
    'banane',
    'inona',
    'course',
    'jour',
    'ia',
    'machine',
    'kiwi',
    'abricot',
    'haricot',
    'mais',
    'manioc',
    'poireau',
    'jus',
    'chaussures',
    'beignet',
    'tomate',
    'igname',
    'culture',
    'tete',
    'histoire',
    'recit',
    'yeti',
    'anime',
    'pomme',
    'torchon',
    'torche',
    'plasma',
    'famille',
    'maman',
    'cours',
    'dos',
    'cartes',
    'mille',
    'souris'
]
mot = lambda : random.choice(mots)
# mot = random.choice(mots)
print(mot())
coups = 15