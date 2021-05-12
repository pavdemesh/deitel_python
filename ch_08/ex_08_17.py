# Exercise 08_17 from Deitel: Intro to Python and CS

"""
Write a regular expression that searches a string and matches a valid number.
A number can have any number of digits, but it can have only digits and a decimal point and possibly a leading sign.
The decimal point is optional, but if it appears in the number, there must be only one,
and it must have digits on its left and its right.
There should be whitespace or a beginning or end-of-line character on either side of a valid number.
"""

import re

# Variation 1: split all numbers by space and store as list items.
# Then check every individual item in the list if it is a valid number.

# Get input from user and print it
text = input()
text_split = text.split()

# Define matching pattern pattern
pattern1 = r"[+-]?((\d+\.\d+)|(\d+))"
pattern2 = r"[+-]?([0-9]+[.])?[0-9]+"

# Check every number against the pattern:
for number in text_split:
    if re.fullmatch(pattern1, number):
        print(f"Number {number} is a valid number")
    else:
        print(f"Number {number} is not a valid number")
