#!/bin/python3

list_input = input("Enter text here: ")
list_output = list_input.split()
print("List of input: ", list_output)

counter = 0
result = [] 

for item in list_output:
    if len(item) > 1 and item[0] == item[-1]:
        counter += 1
        result.append(item)

print(counter)
print(result)
