# Exercise 08_18 from Deitel: Intro to Python and CS

"""
Search online for secure password recommendations.
Research existing regular expressions that validate secure passwords.

Two examples of password requirements are:
• Passwords must contain at least five words, each separated by a hyphen, a space, a period, a comma or an underscore.
• Passwords must have a minimum of 8 characters and contain at least one each from uppercase characters,
lowercase characters, digits and punctuation characters (such as characters in '!@#$%<^>&*?').

Write regular expressions for each of the two requirements above, then use them to test sample passwords.
"""

import re

# Get desired password (to be checked) from user
password_for_test = input("Enter a password: ")

# Regular expression for the first requirement
# Passwords must contain at least five words, each separated by a hyphen, a space, a period, a comma or an underscore.
pattern1 = r"(\w+[.,-_]+){4}\w+\S*"

# Regular expression for the second requirement
# Passwords must have a minimum of 8 characters and must contain at least one each from:
# uppercase characters,lowercase characters, digits and punctuation characters (such as characters in '!@#$%<^>&*?').
pattern2 = r"(?=.*?[A-Z])(?=.*?[a-z)(?=.*?[0-9)(?=.*?[!@#$%<^>&*?]).{8,}"

# Run check 1
if re.fullmatch(pattern1, password_for_test):
    print("Test 1 passed.")
else:
    print("Test 1 failed.")

# Run check 2
if re.fullmatch(pattern2, password_for_test):
    print("Test 2 passed.")
else:
    print("Test 2 failed.")
