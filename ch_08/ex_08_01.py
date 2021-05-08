# Exercise 08_01 from Deitel: Intro to Python and CS

"""
Check-writing systems often insert leading asterisks to prevent alteration and protect the amount as follows:
**399.87
--------
01234567

Write a script that inputs a dollar amount.
Then prints the amount in check-protected format in a field of 10 characters with leading asterisks if necessary.
Hint: In a format string that explicitly specifies alignment with <, ^ or >,
you can precede the alignment specifier with the fill character of your choice.]
"""

# Get amount from user
amount = input()

# Default amount if user inputted nothing
if len(amount) == 0:
    amount = "456.78"

# Display formatted result with leading asterisks
print(f'{amount:*>10}')
