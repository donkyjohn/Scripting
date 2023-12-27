#!/bin/python3
import re
pwd = input("\n Give a valid password: ")
x = True
while x:
    if (len(pwd)<6 or len(pwd)>16) \
        or not re.search("[a-z]",pwd) \
        or not re.search("[0-9]",pwd) \
        or not re.search("[A-Z]",pwd) \
        or not re.search("[$#@]",pwd):
        print("\n NOT a valid password!")
        pwd = input("\n Give a valid password: ")
    else:
        print("Valid password.")
        x = False
        