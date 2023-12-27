#!/bin/python3

import itertools as it  

# infinite iterators

counter = it.count(start=0, step=1)
evenlist = list(next(counter) for _ in range(10))
print(evenlist)

for i in it.count(start=0, step=-1):
      print(i)
      if i == -10:
            break
      
c = 0
for i in it.cycle([-1, 0, 1]):
        print("[{}]{}".format(c, i))
        c += 1
        if c > 10:
                break
        
for i in it.accumulate(range(11)): 
    print(i)   

for n in it.chain('abc', 'def'): 
    print("{}".format(n), end=' ')

for y in it.chain.from_iterable(['abc', 'def']): 
    print(y, end=' ')

for x in it.compress('abcdef', [1,0,1,0,1,1]): 
    print(x, end=' ')

for x in it.dropwhile(lambda x: x<5, [1,4,6,4,1]):
    print(x, end=' ') 
 #   removes the first 1 and 4 because they are smaller than 5 but stops at 6 because it is bigger than 5

for x in it.filterfalse(lambda x: x<5, [1,2,3,4,5,6,7,8,9,10]):
    print(x, end=' ')
    # removes all the numbers smaller than 5

for x in it.groupby([1,2,3,4,5,6,7,8,9,10], lambda x: x<5):
    print(x, end=' ')
    # groups the numbers in 2 groups, the first group is smaller than 5 and the second group is bigger than 5
    # the first group is True and the second group is False 

for x,y in it.groupby([1,2,3,4,5,6,7,8,9,10], lambda x: x<5):
    print(x, list(y))
    # groups the numbers in 2 groups, the first group is smaller than 5 and the second group is bigger than 5
    # the first group is True and the second group is False 
    # prints the numbers in the groups

for x in it.islice(range(10), 5):
       print(x, end=' ')
        # prints the first 5 numbers of the range