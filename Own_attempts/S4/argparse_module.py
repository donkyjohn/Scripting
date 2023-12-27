import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='A script that processes data from a file.')

# Add positional argument
parser.add_argument('input_file', type=str, help='Input file name')

# Add optional argument with default value
parser.add_argument('-o', '--output', type=str, default='output.txt', help='Output file name')

# Parse the command-line arguments
args = parser.parse_args()

# Access the parsed arguments
input_file = args.input_file
output_file = args.output

# Now you can use input_file and output_file in your script
# on the command line: python python_script.py input.txt -o output.txt
# For example, you can open the input file and read its contents
# with open(input_file, 'r') as f:
   # data = f.read()

