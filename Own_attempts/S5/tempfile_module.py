#!/bin/pymol3
import os
import tempfile

# Create a temporary file and write some data to it
fp = tempfile.TemporaryFile() # Create temporary file
fp.write(b'Hello world!') # Write to file
fp.seek(0)  # Read from the beginning of the file
data = fp.read() # Read file
fp.close() # Close file
print(data) # Print data

# Create a temporary directory
dir = tempfile.TemporaryDirectory() # Create temporary directory
print(dir) # Print directory
dir.cleanup() # Remove directory


# Create a temporary file using a context manager
with tempfile.TemporaryFile() as fp:
    fp.write(b'Hello world!')
    fp.seek(0)
    print(fp.read())

# Create a temporary directory using a context manager
with tempfile.TemporaryDirectory() as dir:
    print(dir)


# Create a temporary file using mkstemp()
fp = tempfile.mkstemp() # Create temporary file
print(fp) # Print file
os.close(fp[0]) # Close file
os.remove(fp[1]) # Remove file

# Create a temporary directory using mkdtemp()
dir = tempfile.mkdtemp() # Create temporary directory
print(dir) # Print directory
os.rmdir(dir) # Remove directory


# Create a temporary file using NamedTemporaryFile()
fp = tempfile.NamedTemporaryFile() # Create temporary file
print(fp.name) # Print file name
fp.close() # Close file

tempfile.gettempdir() # Get temporary directory
tempfile.gettempprefix() # Get prefix for temporary files
tempfile.gettempdirb() # Get temporary directory as bytes
tempfile.gettempprefixb() # Get prefix for temporary files as bytes



