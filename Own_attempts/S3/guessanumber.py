#!/bin/python3
number = int(input("Guess a number between 1 and 9: "))
import random
number_to_guess = random.randint(1, 9)

while number != number_to_guess:
    if number > number_to_guess:
        print("Too high!")
    elif number < number_to_guess:
        print("Too low!")
    number = int(input("Guess again: "))
print("YES! {} that's the number!".format(number_to_guess))

