#!/bin/pymol3

inp = list(input("Enter a list of numbers: ").split())  
lst = []
total = 0
for i in inp:
    lst.append(int(i))
    total += int(i)
average = total / len(lst)
print("Total: {}".format(total))
print("Average: {}".format(average))
