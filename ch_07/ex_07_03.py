# Exercise 07_03 from Deitel: Intro to Python for CS

"""
Create a 3-by-3 array containing the even integers from 2 through 18.
Create a second 3-by-3 array containing the integers from 9 down to 1.
Multiply the first array by the second.
"""

import numpy as np

# Create a 3-by-3 array containing the even integers from 2 through 18.
arr1 = np.arange(2, 19, 2).reshape(3, 3)
print(arr1)

print()

# Create a second 3-by-3 array containing the integers from 9 down to 1.
arr2 = np.arange(9, 0, -1).reshape(3, 3)
print(arr2)

print()

# Multiply the first array by the second.
arrs_multiplied = arr1 * arr2
print(arrs_multiplied)
