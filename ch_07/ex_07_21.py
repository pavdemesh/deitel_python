# Exercise 07_21 from Deitel: Intro to Python for CS

"""
In this chapter, we discussed shallow vs. deep copies of arrays.
Python’s built-in list and dictionary types have copy methods that perform shallow copies.

Using the following dictionary ---> dictionary = {'Sophia': [97, 88]}
demonstrate that a dictionary’s copy method indeed performs a shallow copy.

To do so, call copy to make the shallow copy, modify the list stored in the original dictionary,
then display both dictionaries to see that they have the same contents.

Next, use the copy module’s deepcopy function to create a deep copy of the dictionary.
Modify the list stored in the original dictionary,
then display both dictionaries to prove that each has its own data.
"""

from copy import deepcopy

# Create dictionary with  mutable list as value
dictionary = {'Sophia': [97, 88]}

# Call copy to make the shallow copy,
shallow_copy = dictionary.copy()

# Use the copy module’s deepcopy function to create a deep copy of the dictionary.
deep_copy = deepcopy(dictionary)

# Modify the list stored in the original dictionary
dictionary['Sophia'][0] = 22

# Display original dictionary and both copies to see if they have the same contents.
print("\nDisplaying original dictionary after modifying the list in the original: ")
print(dictionary)

print("\nDisplaying shallow copy dictionary after modifying the list in the original: ")
print(shallow_copy)

print("\nDisplaying deep copy dictionary after modifying the list in the original: ")
print(deep_copy)
