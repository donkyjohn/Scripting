#!/bin/python3
import itertools as it

list = [('cadherin','CDH1'),('caspase','CASP3'),
        ('caspase','CASP7'),('cadherin','CDHR1'),
        ('caspase','CASP9'),('cadherin','CDH15'),
        ]

sortedlist = sorted(list)
print("\n", sortedlist)

for key, group in it.groupby(sortedlist, lambda make: make[0]):
    print("*** KEY = {}, GROUP = {}".format(key,group))
    for family, gene in group:
           print('{gene} from {family} gene family'.format(gene=gene,family=family))
           print("*** END OF FAMILY ***\n")
