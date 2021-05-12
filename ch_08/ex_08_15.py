# Exercise 08_15 from Deitel: Intro to Python and CS

"""
Use regular expressions and the findall function to count the number of:
digits, non-digit characters, whitespace characters and words in a string.
"""

import re

# Get input from user and print it
text = input()
print(text)

# Count digits
count_digits = re.findall(r"\d", text)
print(f"Count of digits is: {len(count_digits)}")

# Count whitespaces
count_whitespaces = re.findall(r"\s", text)
print(f"Count of whitespaces is: {len(count_whitespaces)}")

# Count words
count_words = re.findall(r"[A-Z]*[a-z]+", text)
print(f"Count of words is: {len(count_words)}")

# Count of non-digit characters
count_nondigit = re.findall(r"\D", text)
print(f"Count of nondigit characters is: {len(count_nondigit)}")
