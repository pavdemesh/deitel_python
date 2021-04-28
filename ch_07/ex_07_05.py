# Exercise 07_05 from Deitel: Intro to Python for CS

"""
Create a 2-by-3 array containing the first six powers of 2 beginning with 20.
Flatten the array first with method flatten.
Then flatten the array with ravel.
In each case, display the result then display the original array to show that it was unmodified.
"""

import numpy as np

# Create a 2-by-3 array containing the first six powers of 2 beginning with 20.
arr = np.array([2 ** i for i in range(6)]).reshape(2, 3)
print(arr)
print()

# Flatten the array first with method flatten.
print("Flattened with flatten():")
print(arr.flatten())
print()
print("Original arr unchanged:")
print(arr)

print()

# Flatten the array with ravel.
print("Flattened with ravel()")
print(arr.ravel())
print()
print("Original arr unchanged:")
print(arr)
