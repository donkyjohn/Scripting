#!/bin/python3

import fnmatch
import glob

print("\nVersion 1: using fnmatch module.\n")
# Using fnmatch module
print(fnmatch.fnmatch('file.txt', '*.txt'))     
print(fnmatch.fnmatch('file.txt', '?ile.txt'))
print(fnmatch.fnmatch('file.txt', 'file.txt'))
print(fnmatch.fnmatch('file.txt', 'file?.txt'))
print(fnmatch.fnmatch('file.txt', 'file[1234].txt'))
print(fnmatch.fnmatch('file.txt', 'file[!1234].txt'))
print(fnmatch.fnmatch('file.txt', 'file[1-4].txt'))
print(fnmatch.fnmatch('file.txt', 'file[!1-4].txt'))

print("\nVersion 2: using glob module.\n")
# Using glob module
print(glob.glob('*.txt'))
print(glob.glob('file?.txt'))
print(glob.glob('file*.txt'))
print(glob.glob('file[1234].txt'))
print(glob.glob('file[!1234].txt'))
print(glob.glob('file[1-4].txt'))
print(glob.glob('file[!1-4].txt'))
print(glob.glob('file[0-9].txt'))
print(glob.glob('file[!0-9].txt'))
print(glob.glob('file[a-z].txt'))
print(glob.glob('file[!a-z].txt'))
print(glob.glob('file[A-Z].txt'))
print(glob.glob('file[!A-Z].txt'))
print(glob.glob('file[0-9a-z].txt'))
print(glob.glob('file[!0-9a-z].txt'))
