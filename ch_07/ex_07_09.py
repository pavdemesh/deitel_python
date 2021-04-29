# Exercise 07_09 from Deitel: Intro to Python for CS

"""
Create an array containing the values 1–15, reshape it into a 3-by-5 array.

Use indexing and slicing techniques to perform each of the following operations:
a) Select row 2.
b) Select column 5.
c) Select rows 0 and 1.
d) Select columns 2–4.
e) Select the element that is in row 1 and column 4.
f) Select all elements from rows 1 and 2 that are in columns 0, 2 and 4.
"""

import numpy as np

# Create an array containing the values 1–15, reshape it into a 3-by-5 array.
nums = np.arange(1, 16).reshape(3, 5)
print("Create an array containing the values 1–15, reshape it into a 3-by-5 array:")
print(nums)
print()

# a) Select row 2.
print("a): Select row 2:")
print(nums[2])
print()

# b) Select column 5 (since index 5 will cause an error, I display the last, 5th col with index 4)
print("b): Select column 5 - displaying column index [4] as the last possible column:")
print(nums[:, 4])
print()

# c) Select rows 0 and 1.
print("c): Select rows 0 and 1:")
print(nums[:2])
print()

# d) Select columns 2–4.
print("d): Select columns 2–4:")
print(nums[:, 2:])
print()

# e) Select the element that is in row 1 and column 4.
print("e): Select the element that is in row 1 and column 4:")
print(nums[1][4])
print()

# f) Select all elements from rows 1 and 2 that are in columns 0, 2 and 4.
print("f): Select all elements from rows 1 and 2 that are in columns 0, 2 and 4:")
print(nums[1:3, [0, 2, 4]])
