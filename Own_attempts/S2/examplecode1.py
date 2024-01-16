#!/bin/python3
import itertools as it

def evens():
    n = 0
    while True:
        yield n 
        n += 10
evens = evens()
evenlist =  list(next(evens) for _ in range(10))
print(evenlist)


counter = it.count(start=0, step=2)
evenlist2 = list(next(counter) for _ in range(10))
print(evenlist2)

for i in it.count(start=0, step=-1):
    if i < -3:
        break
    print(i)

c = 1
for i in it.cycle([10,-10]):
    if c > 5:
        break
    print(c,i)
    c+=1

list1 = list(it.accumulate(range(10)))
print(list1)

import operator
list3 = list(it.accumulate(range(1, 5), operator.sub))
print(list3)

families = [('cadherin', 'CDH1'), ('caspase', 'CASP3'),
            ('caspase', 'CASP7'), ('cadherin', 'CDHR1'),
            ('caspase', 'CASP9'), ('cadherin', 'CDH15')]

print(families)
sort = sorted(families)
print("\n", sort)

for k, v in it.groupby(sort, lambda make: make[0]):
    print(k, v)
    for family, gene in v:
        print('{gene} from {family} gene family'.format(gene=gene,family=family))



