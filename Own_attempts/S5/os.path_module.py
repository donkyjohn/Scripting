#!/bin/pymol3

import os

path = os.getcwd()
var = os.path.split(path) # Split path into head and tail
print(var)

var2 = os.path.dirname(path)
print(var2)

var3 = os.path.basename(path)
print(var3)

var4 = os.path.splitdrive(path)
print(var4)

var5 = os.path.exists(path)
print(var5) # if path exists, True, else False

var6 = os.path.isfile(path)
print(var6) # if there is a file in path return True, else False

var7 = os.path.isdir(path)
print(var7) # if there is a directory in path return True, else False

var8 = os.path.getsize(path)
print(var8) # return size of file in bytes

# os.stat(path) to get status of file or directory
statinfo = os.stat('somefile.txt')

# to get size of file in bytes
size = os.statinfo.st_size  # in bytes

# file type and permission
mode = os.statinfo.st_mode

# time most recent content modification
mtime = os.statinfo.st_mtime
