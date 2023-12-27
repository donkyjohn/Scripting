#!bin/python3

import itertools as it
import re 
import random

UpperRanks = ['A', 'K', 'Q', 'J']
LowerRanks = ['10', '9', '8', '7', '6', '5', '4','3', '2']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

deck = list(it.product(UpperRanks, suits)) + list(it.product(LowerRanks, suits))
shuffle1 = random.shuffle(deck)
print("\nDECK1:")
print(deck)

shuffle2 = random.shuffle(deck)
print("\nDECK2:")
print(deck)


