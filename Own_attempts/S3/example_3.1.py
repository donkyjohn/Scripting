#!/bin/python3
M = [[i + j for j in range(3)] for i in range(1, 8, 3)]
print("Row 1:", M[0])
print("Row 2:", M[1])
print("Row 3:", M[2])

print("\nRow 2:", M[1])
print("Item 1 in row 2:", M[1][0])

col1 = [row[0] for row in M]
print("\nCollected items in column 1:", col1) 

col2 = [row[1] for row in M]
print("Collected items in column 2:", col2)

col3 = [row[2] for row in M]    
print("Collected items in column 3:", col3)

col1plus1 = [row[0] + 1 for row in M]
print("\ncol1:", col1, "versus col1plus1:", col1plus1)

col2plus1 = [row[1] + 2 for row in M]
print("col2:", col2, "versus col2plus2:", col2plus1)

col3plus1 = [row[2] + 3 for row in M]
print("col3:", col3, "versus col3plus3:", col3plus1)

col1even = [row[0] for row in M if row[0] % 2 == 0]
print("\nFiltered even items in column 1:", col1even)   

diagonal = [M[i][i] for i in [0, 1, 2]]
print("\nDiagonal from M:", diagonal)

list10 = list(range(-100, 101, 10))
print("\nlist10:", list10)

multiples = [[x, x / 10, x * 10] for x in range(-100, 101, 10) if x > 0]
print("multiples:", multiples)

peptides = ['MATGCY','GPSALVIMWAIL','RKGDPALEKG','SMALLY']
peplen = {pept:len(pept) for pept in peptides}
print("\npeptides =", peptides, "\nresult =", peplen)

reversedict = {v:k for k,v in peplen.items()}
print("\nrevdict = {}".format(reversedict))