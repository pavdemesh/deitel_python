# Exercise 08_08 from Deitel: Intro to Python and CS

"""
Modify the previous exercise to display 10 emojis beginning with the smiley face, which has the value 0x1F600:5
The value 0x1F600 is a hexadecimal (base 16) integer.
See the online appendix “Number Systems” for information on the hexadecimal number system.
 ou can find emoji codes by searching online for “Unicode full emoji list.”
 The Unicode website precedes each character code with "U+" (representing Unicode).
 Replace "U+" with "0x" to properly format the code as a Python hexadecimal integer."""

for i in range(10):
    print(f'{0x1F600 + i:c}')

print("--------")

for i in range(10):
    print(f'{128512 + i:c}')
