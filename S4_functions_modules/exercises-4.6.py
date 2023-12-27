#!/usr/bin/python3
################################################################################
# 4.6 Modules: validity of password input 
################################################################################
import re
# First try to check password conditions with if
print("\nVersion 1: check each condition.\n")
pw = input("\nGive a valid password: ")
x = True
while x:  
    if (len(pw)<6 or len(pw)>12):
        break
    elif not re.search("[a-z]",pw):
        break
    elif not re.search("[0-9]",pw):
        break
    elif not re.search("[A-Z]",pw):
        break
    elif not re.search("[$#@]",pw):
        break
    else:
        print("Valid password\n")
        x = False
        break
if x:
    print("NOT a valid password\n")
################################################################################
print("\nVersion 2: ask for password as long as it is invalid.\n")
# Using while loop to keep on asking for password as long as it is invalid
x = True
while x:
    pw = input("Give a valid password: ")
    if(len(pw)<6 or len(pw)>12) \
        or not re.search("[0-9]",pw) \
        or not re.search("[a-z]",pw) \
        or not re.search("[A-Z]",pw) \
        or not re.search("[$#@]",pw):
        print("NOT a valid password!!!")
    else:
        print("Valid password.")
        x = False
################################################################################