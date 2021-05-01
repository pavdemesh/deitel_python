# Exercise 07_17 from Deitel: Intro to Python for CS

"""
Research the NumPy bincount function.
Create a 5-by-5 array (arr) of random integers in the range 0–99.
Use the NumPy bincount function to count the number of occurrences of each non-negative integer in arr.
"""

import numpy as np

# Create 5-by-5 array with random ints in the range 0–99
# I will create a 12-by-12 array
arr = np.random.randint(low=0, high=100, size=(12, 12))
print(arr)
print()

# Count bins passing as argument to bincount a flattened array
counts = np.bincount(arr.flatten())
print(f"Total occurrences of 12 are: {counts[12]}")
print(f"Total occurrences of 35 are: {counts[35]}")
print(f"Total occurrences of 99 are: {counts[99]}")

print()
# Display the whole array of counts
print("Full array of counts looks like this:")
print(counts)
