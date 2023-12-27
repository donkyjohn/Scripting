import re

def sort_string_by_separator():
    inputA = input("Enter a string: ")
    inputb = input("Enter a character to split by: ")

    inputA1 = str(inputA)
    inputb1 = str(inputb)

    inputA2 = re.sub('\s', inputb1, inputA1) 
    inputA3 = inputA2.split(inputb1)
    inputA3.sort()
    inputA4 = inputb1.join(inputA3)
    print(inputA4)

sort_string_by_separator()



