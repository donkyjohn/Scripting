#!/bin/python3

listnr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
strlist = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numberstuple = ('ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE')

for i in zip(listnr, strlist, numberstuple):
    print(i)

import random

print(random.randrange(1, 10))  # random number between 1 and 9
print(random.randrange(1, 10, 2))  # random number between 1 and 9, uneven  numbers only
print(random.randrange(0, 101, 5))  # random number between 0 and 100, 5 steps  
print(random.random())  # random number between 0 and 1 (float)
print(random.uniform(1, 10))  # random number between 1 and 10 (float)  
print(random.choice(strlist))  # random string from list 
print(random.sample(strlist, 3))  # random 3 strings from list
print(random.shuffle(strlist))  # shuffle list
print(random.randint(1, 10))  # random number between 1 and 10 (int)    

myrange = range(1, 51)
ntseq = ""
for i in myrange:
    nt = random.choice(['A', 'T', 'C', 'G'])
    ntseq = ntseq + nt

print("Random nucleotide sequence: {}".format(ntseq))


