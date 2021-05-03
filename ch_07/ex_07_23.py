# Exercise 07_23 from Deitel: Intro to Python for CS

"""
Perform the following tasks with pandas DataFrames:
a) Create a DataFrame temperatures from a dictionary of three temperature readings each
for 'Maxine', 'James' and 'Amanda'.

b) Recreate the DataFrame temperatures in Part (a) with custom indices using the index keyword argument
and a list containing 'Morning', 'Afternoon' and 'Evening'.

c) Select from temperatures the column of temperature readings for 'Maxine'.

d) Select from temperatures the row of 'Morning' temperature readings.

e) Select from temperatures the rows for 'Morning' and 'Evening' temperature readings.

f) Select from temperatures the columns of temperature readings for 'Amanda' and 'Maxine'.

g) Select from temperatures the elements for 'Amanda' and 'Maxine' in the 'Morning' and 'Afternoon'.

h) Use the describe method to produce temperatures’ descriptive statistics.

i) Transpose temperatures.

j) Sort temperatures so that its column names are in alphabetical order.
"""

import pandas as pd
import numpy as np


# a) Create a DataFrame temperatures from a dictionary of three temperature readings
# each for 'Maxine', 'James' and 'Amanda'.
print("a):")
temps_dict = {"Maxine": [95, 96, 97], "James": [45, 46, 47], "Amanda": [75, 76, 77]}
temps = pd.DataFrame(temps_dict)

# b) Recreate the DataFrame temperatures in Part (a) with custom indices using the index keyword argument
# and a list containing 'Morning', 'Afternoon' and 'Evening'.
print("\nb):")
temperatures = pd.DataFrame(temps_dict, index=['Morning', 'Afternoon', 'Evening'])
print(temperatures)

# c) Select from temperatures the column of temperature readings for 'Maxine'.
print("\nc):")
print(temperatures["Maxine"])
print(temperatures.Maxine)

# d) Select from temperatures the row of 'Morning' temperature readings.
print("\nd):")
print(temperatures.loc["Morning"])
print(temperatures.iloc[0])

# e) Select from temperatures the rows for 'Morning' and 'Evening' temperature readings.
print("\ne):")
print(temperatures.loc[["Morning", "Evening"]])
print(temperatures.iloc[[0, 2]])

# f) Select from temperatures the columns of temperature readings for 'Amanda' and 'Maxine'.
print("\nf):")
print(temperatures[["Amanda", "Maxine"]])
print(temperatures.loc[:, ["Amanda", "Maxine"]])

# g) Select from temperatures the elements for 'Amanda' and 'Maxine' in the 'Morning' and 'Afternoon'.
print("\ng):")
print(temperatures.loc[["Morning", "Afternoon"], ["Amanda", "Maxine"]])
print(temperatures.iloc[:2, [0, 2]])

# h) Use the describe method to produce temperatures’ descriptive statistics.
print("\nh):")
print(temperatures.describe())

# i) Transpose temperatures.
print("\ni):")
print(temperatures.T)

# j) Sort temperatures so that its column names are in alphabetical order.
print("\nj):")
print(temperatures.sort_index(axis=1))
