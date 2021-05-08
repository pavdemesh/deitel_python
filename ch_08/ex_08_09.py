# Exercise 08_09 from Deitel: Intro to Python and CS

"""
Write a script that reads a five-letter word from the user
and produces every possible three-letter string, based on the word’s letters.
For example, the three-letter words produced from the word “bathe" include:
 “ate,” “bat,” “bet,” “tab,” “hat,” “the” and “tea.”
Challenge: Investigate the functions from the itertools module, then use an appropriate function to automate this task.
"""

import itertools

source_word = input("Enter a word or the program will use 'bathe' by default: ")
if len(source_word) == 0:
    source_word = 'bathe'

# With itertools
# Create a list of tuples with all possible permutations
possible_combinations = [''.join(word) for word in itertools.permutations(source_word, 3)]

# Display result from itertools
print("-------------------------------")
print("Combinations generated with itertools are:")
print(*possible_combinations, sep=", ")
print("-------------------------------")


# Without itertools
# Define custom function
def gen_permutations(word, list_to_store, length=3, prefix=None):
    """
    Generates all possible 3-letter (default) combinations from a given word and stores them in a list provided as arg
    :param word: Word from which to take chars to generate combinations
    :param length: Int, desired length of generated combinations (3 by default)
    :param prefix: Already generated part of the 3-letter combination
    :param list_to_store: list defined outside the function to store generated combinations
    :return: None. Modifies the list provided as argument by appending all combinations to it
    """
    # Uses provided prefix or create empty string if no prefix provided
    prefix = prefix or ""

    # If required length reached - append combination to the list and return None
    if length == 0:
        list_to_store.append(prefix)
        return

    # Else: call gen_permutations on already existing prefix with chars from word that are unused by now:
    for char in word:
        # If this char is already in prefix - skip
        if char in prefix:
            continue
        gen_permutations(word, list_to_store, length-1, prefix+char)


# Initialize empty list to keep combinations
possible_strings = []

# Generate combinations and store them to the list
gen_permutations(source_word, possible_strings)

# Display result
print("Combinations generated with custom function are:")
print(*possible_strings, sep=", ")
print("-------------------------------")

# Compare two lists
print(f"Comparison of two lists returned: {possible_strings == possible_combinations}")
