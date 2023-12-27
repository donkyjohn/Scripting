import sys

def reverse(*args):
    reversed_args = []
    for arg in args:
        reversed_args.append(arg[::-1])
    return reversed_args

if len(sys.argv) > 1:
    result = reverse(*sys.argv[1:])
    print(' '.join(result)) 
else:
    print("Please provide arguments from the command line.")

