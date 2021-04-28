# Exercise 07_02 from Deitel: Intro to Python for CS

"""
Use arange to create a 2-by-2 array containing the numbers 0–3.
Use broadcasting to perform each of the following operations on the original array:
a) Cube every element of the array.
b) Add 7 to every element of the array.
c) Multiply every element of the array by 2.
"""

import numpy as np

# Use arange to create a 2-by-2 array containing the numbers 0–3.
arr = np.arange(4).reshape(2, 2)
print(arr)

# a) Cube every element of the array.
arr_cubed = arr ** 3
print(arr_cubed)

# b) Add 7 to every element of the array.
arr_added = arr + 7
print(arr_added)

# c) Multiply every element of the array by 2.
arr_multiplied = arr * 2
print(arr_multiplied)
