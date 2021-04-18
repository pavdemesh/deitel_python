"""
Insert 20 random letters in the range 'a' through 'f' into a list.
"""

import random

rand_chars_list = list()
letters = "abcdef"

for i in range(20):
    rand_index = random.randrange(6)
    rand_chars_list.append(letters[rand_index])

# a) Sort the list in ascending order
rand_chars_list.sort()
print(rand_chars_list)

print("-----------------------------------------------------------")

# b) Sort the list in descending order
rand_chars_list.sort(reverse=True)
print(rand_chars_list)

print("-----------------------------------------------------------")

# c) Get the unique values sort them in ascending order
unique_chars = list()
for char in rand_chars_list:
    if char not in unique_chars:
        unique_chars.append(char)
unique_chars.sort()
print(unique_chars)
