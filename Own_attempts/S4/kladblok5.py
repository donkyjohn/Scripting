#!/bin/python3
import itertools as it
import time

def evens():
    n = 0
    while True:
        yield n
        n += 2
even = evens()
evenlist = list(next(even) for _ in range(10))
print("The long way (7 lines):{}".format(evenlist))

counter = it.count(start=0, step=2)
evenlist = list(next(counter) for _ in range(10))
print("The short way (3 lines):{}".format(evenlist))

print("Negative count:")
print(("-"*20))
for i in it.count(start=0, step=-5):
    time.sleep(0.1)
    if i == -10:
        break
    print(i)

c = 0
for i in it.cycle([-1, 0, 1]):
    time.sleep(0.1)
    if c > 10:
        break
    print("[{}]".format(c, i))
    c += 1
