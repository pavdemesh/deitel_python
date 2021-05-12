# Exercise 08_16 from Deitel: Intro to Python and CS

"""
Use a regular expression to search through a string and to locate all valid URLs.
For this exercise, assume that a valid URL has the formhttp://www.domain_name.extension,
where extension must be two or more characters.
"""

import re

# Get input from user and print it
text = input()
print(text)

# Find all matching patterns
valid_urls = re.findall(r"\bhttp://www.[a-z]+.[a-z]{3,}", text)
print(valid_urls)
