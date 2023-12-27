#!/bin/python3

import humanfriendly as hf

print("\nSize of file in bytes: ", hf.format_size(123456789, binary=True))