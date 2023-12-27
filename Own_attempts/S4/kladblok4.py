#!/bin/python3

import random 
import time

RPSlist = ["rock", "paper", "scissors"]
print("Welcome to Rock, Paper, Scissors!")
print("\nPlease choose one of the following: rock, paper, scissors")
userchoice = input("Your choice: ")
print("rock...")
time.sleep(1)
print("paper...")
time.sleep(1)
print("scissors...")
time.sleep(1)
compchoice = random.choice(RPSlist)


if userchoice == compchoice:
    print("It's a tie!")
elif userchoice == "rock" and compchoice == "paper":
    print("U lost against the computer!, it chose: " + compchoice)
elif userchoice == "rock" and compchoice == "scissors":
    print("U won against the computer!, it chose: " + compchoice)
elif userchoice == "paper" and compchoice == "rock":
    print("U won against the computer!, it chose: " + compchoice)
elif userchoice == "paper" and compchoice == "scissors":
    print("U lost against the computer!, it chose: " + compchoice)
elif userchoice == "scissors" and compchoice == "rock":
    print("U lost against the computer!, it chose: " + compchoice)
elif userchoice == "scissors" and compchoice == "paper":
    print("U won against the computer!, it chose: " + compchoice)
else:
    print("Please choose one of the following: rock, paper, scissors")
    userchoice = input("Your choice: ")
    print("You chose: " + userchoice)


