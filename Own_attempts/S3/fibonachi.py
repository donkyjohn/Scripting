#!/bin/python3

# fibonacci.py

x, y = 0, 1
while x < 50:
    r = x + y
    if r > 50:
        break
    print(r)
    x = y
    y = r
