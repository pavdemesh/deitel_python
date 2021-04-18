"""
Starting with a list containing 1 through 10, use filter, map and sum to calculate
the total of the triples of the even integers from 2 through 10.
Reimplement your code with list comprehensions rather than filter and map
"""
# Create list of ints from 1 through 10
nums = list(range(1, 11))

# Calculating sum of evens' triples by using map() and filter()
sum_with_map_filter = sum(map(lambda x: x * 3, filter(lambda x: x % 2 == 0, nums)))
print(sum_with_map_filter)

# Calculate sum of evens' triples by using list comprehensions
sum_with_comprehension = sum([x * 3 for x in nums if x % 2 == 0])
print(sum_with_comprehension)
