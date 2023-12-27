#!/bin/python3

directory = {'Belgium' : 'Brussels', 'Germany' : 'Berlin', 'France' : 'Paris', 'Spain' : 'Madrid', 'Italy' : 'Rome', 'Greece' : 'Athens', 'Austria' : 'Vienna', 'Poland' : 'Warsaw', 'Denmark' : 'Copenhagen', 'Finland' : 'Helsinki', 'Sweden' : 'Stockholm', 'Norway' : 'Oslo', 'Netherlands' : 'Amsterdam'}
print("List of countries and their capitals:")
print("="*40)
for k, v in directory.items():
    print(k.ljust(15), v)
