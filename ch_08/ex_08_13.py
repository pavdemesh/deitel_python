# Exercise 08_13 from Deitel: Intro to Python and CS

"""
Check whether a sentence contains more than one space between words.
If so, remove the extra spaces and display the results.
For example, 'Hello World' should become 'Hello World'.
"""

import re

# Get input from user
text = input()

# Substitute one or more consecutive spaces with a single space
cleaned_text = re.sub(r" +", " ", text)

# Display result
print(cleaned_text)
