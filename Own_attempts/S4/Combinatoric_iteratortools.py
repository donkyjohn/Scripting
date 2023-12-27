import itertools

# itertools.product() - Cartesian product of input iterables
# Generates all possible combinations of the elements from the input iterables
product_result = itertools.product([1, 2], ['a', 'b'])
print(list(product_result))  # Output: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

# itertools.permutations() - Generates all possible permutations of the input iterable
permutations_result = itertools.permutations([1, 2, 3])
print(list(permutations_result))  # Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# itertools.combinations() - Generates all possible combinations of the input iterable
combinations_result = itertools.combinations([1, 2, 3], 2)
print(list(combinations_result))  # Output: [(1, 2), (1, 3), (2, 3)]

# itertools.combinations_with_replacement() - Generates all possible combinations of the input iterable with replacement
combinations_with_replacement_result = itertools.combinations_with_replacement([1, 2], 2)
print(list(combinations_with_replacement_result))  # Output: [(1, 1), (1, 2), (2, 2)]

# itertools.chain() - Chains multiple iterables together as a single iterable
chain_result = itertools.chain([1, 2], ['a', 'b'])
print(list(chain_result))  # Output: [1, 2, 'a', 'b']

# itertools.islice() - Returns an iterator that returns selected elements from the input iterable
islice_result = itertools.islice([1, 2, 3, 4, 5], 2, 4)
print(list(islice_result))  # Output: [3, 4]

# itertools.count() - Returns an iterator that generates consecutive integers
count_result = itertools.count(start=1, step=2)
print(list(itertools.islice(count_result, 5)))  # Output: [1, 3, 5, 7, 9]

# itertools.cycle() - Returns an iterator that cycles through the elements of the input iterable indefinitely
cycle_result = itertools.cycle([1, 2, 3])
print(list(itertools.islice(cycle_result, 5)))  # Output: [1, 2, 3, 1, 2]

# itertools.repeat() - Returns an iterator that repeats the specified element indefinitely or a specified number of times
repeat_result = itertools.repeat('a', 3)
print(list(repeat_result))  # Output: ['a', 'a', 'a']
