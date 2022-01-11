# Exercise 10_07 from Deitel: Intro to Python and CS

"""
The Python Standard Library’sdatetime module contains a datetime class for manipulating dates and times.
The class provides various overloaded operators.
Research class datetime’s capabilities, then perform the following tasks:
a) Get the current date and time and store it in variable x.
b) Repeat Part (a) and store the result in variable y.
c) Display each datetime object.
d) Display each datetime object’s data attributes individually.
e) Use the comparison operators to compare the two datetime objects.
f) Calculate the difference between y and x.
"""

import datetime
import random
import time

# a) Get the current date and time and store it in variable x.
x = datetime.datetime.now()

# Make random pause
time.sleep(random.randint(0, 4))
time.sleep(random.random())

# b) Repeat Part (a) and store the result in variable y.
y = datetime.datetime.now()

# c) Display each datetime object.
print(x)
print(y)

# d) Display each datetime object’s data attributes individually.
print(x.date())
print(y.hour)
print(x.month)

# e) Use the comparison operators to compare the two datetime objects.
print(x > y)
print(x != y)

# f) Calculate the difference between y and x.
print(y - x)
