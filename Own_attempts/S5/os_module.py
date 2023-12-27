#!/bin/python3

import os
import time

pwd = os.getcwd() # Get current working directory
print("\nCurrent working directory: ", pwd)

# Change directory
print("\nChanging directory to /home/guest...")
time.sleep(1) 
os.chdir("/home/guest")
print("\nDirectory changed successfully to {}.".format(os.getcwd()))

test_dir = "/home/guest/test"
file_path = "/home/guest/test/test.txt"  # Replace with the actual file path

print("\nRemoving excess files and directories...")
time.sleep(1) 

if os.path.exists(file_path):   # Check if file exists
        os.remove(file_path)    # Remove file
        print("File in {} removed successfully.".format(test_dir))
        time.sleep(1)
else:
        time.sleep(1)
        print("File can't be found in {}.".format(test_dir))

if os.path.exists(test_dir): # Check if directory exists
    os.rmdir(test_dir) # Remove directory
    print("Directory \"{}\" removed successfully.".format(test_dir))
    time.sleep(1)
else:
    print("Directory does not exist.")
    time.sleep(1)

print("\nCreating test directory...")
time.sleep(1)
os.mkdir("test") # Create directory
print("\n Test directory created successfully.")
time.sleep(1)
print("\n Changing directory to test directory...")
time.sleep(1) # Pause for 2 seconds

os.chdir("test") # Change directory

print("\nDirectory changed successfully to {}.".format(os.getcwd()))
time.sleep(1)

print("\nCreating test.txt file...")
time.sleep(1)
with open("test.txt", "w") as f: # Create file
    f.write("Hello world!") # Write to file
    f.close() # Close file
print("\nFile \"{}\" created successfully.".format(os.path.basename(f.name)))
time.sleep(1)

print("\nChanging directory back to original...")
time.sleep(1) # Pause for 2 seconds
os.chdir(pwd) # Change directory back to original
print("\nDirectory changed successfully to {}.".format(os.getcwd()))

hostname = os.environ['HOSTNAME'] # Get hostname
print("\nHostname: ", hostname)
print("\nUsername: ", os.environ['USER']) # Get username
print("\nHome directory: ", os.environ['HOME']) # Get home directory
print("\nPath: ", os.environ['PATH']) # Get path
print("\nLANG: ", os.environ['LANG']) # Get language


