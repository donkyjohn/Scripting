#!/bin/python3

var = {x**2 for x in range(20) if x % 2 == 0}

sorted_var = sorted(var)
print(sorted_var)

reversed_var = sorted(var, reverse=True)    
print(reversed_var)

var2 = {x:x**2 for x in range(1, 12) if x % 3 == 0}
print(var2)

var3 = [x**2 for x in range(1, 12) if x % 2 == 0]
sorted_var3 = sorted(var3)
extended_var3 = sorted_var3.extend(reversed_var)
print(sorted_var3)

found_greater_than_100 = False

greater_than_100 = []

for x in sorted_var3:
    if x > 100:
        found_greater_than_100 = True
        greater_than_100.append(x)

if found_greater_than_100:
    print('X values greater than    100:', greater_than_100)
else:
    print('No X is greater than 100')


for x in var:
    while x > 100:
        print('X value greater than 100:', x)
        break

import sys  
sys.stdout.write("Hello, world!\n")    
