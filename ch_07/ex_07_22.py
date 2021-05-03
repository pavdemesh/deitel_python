# Exercise 07_22 from Deitel: Intro to Python for CS

"""
Perform the following tasks with pandas Series:

a) Create a Series from the list [7, 11, 13, 17].
b) Create a Series with five elements that are all 100.0.
c) Create a Series with 20 elements that are all random numbers in the range 0 to 100.

Use method describe to produce the Series’ basic descriptive statistics.

d) Create a Series called temperatures of the floating-point values 98.6, 98.9, 100.2 and 97.9.
Using the index keyword argument, specify the custom indices 'Julie', 'Charlie', 'Sam' and 'Andrea'.

e) Form a dictionary from the names and values in Part (d), then use it to initialize a Series.
"""

import pandas as pd
import numpy as np

# a) Create a Series from the list [7, 11, 13, 17].
print("a) Create a Series from the list [7, 11, 13, 17]:")
nums1 = pd.Series([7, 11, 13, 17])
print(nums1)
print()

# b) Create a Series with five elements that are all 100.0.
print("b) Create a Series with five elements that are all 100.0:")
nums2 = pd.Series(100.0, range(5))
print(nums2)
print()

# c) Create a Series with 20 elements that are all random numbers in the range 0 to 100.
print('c) Create a Series with 20 elements that are all random numbers in the range 0 to 100:')
nums3 = pd.Series(np.random.randint(low=0, high=101, size=20))
print(nums3)
print()

# d) Create a Series called temperatures of the floating-point values 98.6, 98.9, 100.2 and 97.9.
# Using the index keyword argument, specify the custom indices 'Julie', 'Charlie', 'Sam' and 'Andrea'.
print("d) Create a Series with temperatures and custom indices:")
temperatures = pd.Series([98.6, 98.9, 100.2, 97.9], index=['Julie', 'Charlie', 'Sam', 'Andrea'])
print(temperatures)
print()

# e) Form a dictionary from the names and values in Part (d), then use it to initialize a Series.
print("e) Form a dictionary from the names and values in Part (d), then use it to initialize a Series:")
dict_from_series = {name: temperatures[name] for name in temperatures.index}
print("Dictionary formed from Series:")
print(dict_from_series)
series_from_dict = pd.Series(dict_from_series)
print("Series generated from dictionary generated from Series:")
print(series_from_dict)
