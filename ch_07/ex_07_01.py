# Exercise 07_01 from Deitel: Intro to Python for CS

"""
Fill a 2-by-3 array with ones, a 3-by-3 array with zeros and a 2-by-5 array with 7s.
"""

import numpy as np

# Important: dimensions must be specified as a tuple

# Ones with shape 2-by-3
arr_ones = np.ones((2, 3))
print(arr_ones)
print()

# Zeros with shape 3-by-3
arr_zeros = np.zeros((3, 3))
print(arr_zeros)
print()

# Sevens with shape 2-by-5
arr_sevens = np.full((2, 5), 7)
print(arr_sevens)
