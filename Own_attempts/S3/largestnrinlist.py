#!/bin/python3

inp = input("Enter a list of numbers: ").split()
lst = []
for i in inp:
    lst.append(int(i))
print("List: {}".format(lst))
print("Largest number: {}".format(max(lst)))
