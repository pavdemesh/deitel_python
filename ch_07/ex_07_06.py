# Exercise 07_06 from Deitel: Intro to Python for CS

"""
Research in the NumPy documentation the array method astype, which converts an array’s elements to another type.
Use linspace and reshape to create a 2-by-3 array with the values 1.1, 2.2, …, 6.6.
Then use astype to convert the array to an array of integers.
"""

import numpy as np

# Use linspace and reshape to create a 2-by-3 array with the values 1.1, 2.2, …, 6.6.
arr = np.linspace(1.1, 6.6, 6).reshape(2, 3)
print(arr)
print()

# Use astype to convert the array to an array of integers.
arr_ints = arr.astype(dtype=int)
print(arr_ints)
