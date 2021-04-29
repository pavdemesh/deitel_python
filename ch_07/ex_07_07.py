# Exercise 07_07 from Deitel: Intro to Python for CS

"""
NumPy outputs 2D arrays in a nice column-based format that right-aligns every element in a field width.
The field width’s size is determined by the array element value that requires the most character positions to display.

To understand how powerful it is to have this formatting simply built-in:
Write a function that reimplements NumPy’s array formatting for two-dimensional arrays using loops.
Assume the array contains only positive integer values.
"""

import numpy as np


def display_np_style(arr: list):
    """
    Reimplements NumPy’s array formatting for two-dimensional lists using loops
    :param arr: 2D list of positive ints
    :return: Prints out the 2D list with right-aligned in numpy style
    """
    # Calculate longest int by finding largest int and determining its length
    largest = -1
    for row in arr:
        largest = max(largest, max(row))
    longest = len(str(largest)) + 1

    for row in range(len(arr)):
        print("[", end="")
        for col in range(len(arr[row])):
            # Use length of the longest as field width for right alignment
            print(f"{arr[row][col]:>{longest}}", end="")
        print("]")


my_list = [[3334, 56765, 12, 9, 5552343245], [242342, 5, 234, 24242467574, 2], [6424, 77, 452146, 9, 56635244244]]

# Display via custom function
print("Displaying list with self-written function:")
display_np_style(my_list)

print()

# Display with NumPyy functionality
my_arr = np.array(my_list)
print(my_arr)
