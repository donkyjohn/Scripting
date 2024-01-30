#!/bin/python3

# fibonacci.py

x, y = 0, 1
count = 0
while x < 100000000000000000000:
    r = x + y
    if r > 100000000000000000000:
        break
    count += 1
    if count == 50:
        num1 = r
    elif count == 51:
        num2 = r
        break
    x = y
    y = r

result = num2 / num1
print(num1)
print(num2)
print(result)


