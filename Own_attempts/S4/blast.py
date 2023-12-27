#!/bin/python3

import re
import random
import time     

pattern = input("Enter the pattern: ")
DNAregex = re.compile(pattern)

#random nucleotide sequence generator:
#myrange = range(1, 51)
#ntseq = ""  
#for i in myrange:
#    nt = random.choice(['A', 'T', 'C', 'G'])
#    ntseq = ntseq + nt

ntseq = input("Enter the sequence: ")
print(f"nucleo seq: {ntseq}")
time.sleep(1) #sleep for 1 second, requires the import time module

matches = DNAregex.finditer(ntseq)
for match in matches:
    x = match.start()
    tabs = " " * (x + 6)
    tabs2 = " " * (x + 12)
    lines = "|" * len(match.group())
    
    print(f"{tabs2}{lines}")
    print(f"Match:{tabs}{match.group()}")




