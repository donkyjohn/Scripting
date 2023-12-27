#!/bin/python3

import glob
import os

location = "/home/guest/GITHUB/pythonscripts/"
os.chdir(location)
#for filename in glob.iglob('fastqc*'):
    #print(filename)

# glob.iglob() returns an iterator, which is more efficient than glob.glob() which returns a list.
    
# glob.glob() returns a list of all files that match a pattern.
cwd = os.getcwd()
print(cwd)

iternames = glob.iglob('/home/guest/GITHUB/pythonscripts/**/*.py', recursive=True)

for filename in iternames:
    print(filename)

