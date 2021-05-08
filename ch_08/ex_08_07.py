# Exercise 08_07 from Deitel: Intro to Python and CS

"""
Use the c presentation type to display a table of the character codes in the range 0 to 255 and corresponding characters
"""

for i in range(256):
    print(f'character code {i:0>3} corresponds to symbol {i:c}')
