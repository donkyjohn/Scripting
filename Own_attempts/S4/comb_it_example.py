#!/bin/python3

import itertools as it

banknotes = [10, 10, 10, 10, 10, 20, 20, 20, 5, 5, 5, 5]
rev_sort = sorted(banknotes, reverse=True)


combinations = []

for x in range(1, len(rev_sort)+1):  # generate a sequence of numbers from 1 to the length of the list
                                     # the length of the list is 12 so the sequence is 1 to 12, +1 because the last number is not included
    for combination in it.combinations(rev_sort, x): # generate all the combinations of the list with the numbers from the sequence
        if sum (combination) == 100:             # if the sum of the combination is 100
            combinations.append(combination)    # add the combination to the list combinations
print(len(set(combinations)))                  # print the length of the list combinations, set removes the duplicates
    
