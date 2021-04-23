"""
Recall that strings are sequences of characters. 
Write a script that:
1) inputs a sentence from the user, 
2) then uses a dictionary to summarize the number of occurrences of each letter. 
Ignore case, ignore blanks and assume the user does not enter any punctuation. 
3) Display a two-column table of the letters and their counts with the letters in sorted order. 
4) Challenge: Use a set operation to determine which letters of the alphabet were not in the original string.
"""

import string


def get_unique_chars(text):
    """
    Input: a string without punctuation.
    Return: Dictionary with unique chars and their count.
    IGNORES: Case and spaces
    """
    unique_chars_with_count = dict()
    for letter in text.lower():
        if letter in string.ascii_lowercase:
            unique_chars_with_count[letter] = unique_chars_with_count.get(letter, 0) + 1
    return unique_chars_with_count


def display_sorted_dictionary_two_cols(dict_to_display):
    """
    Receives a dictionary. Returns None.
    Prints the dictionary in two column format sorted by keys
    """
    for k, v in sorted(dict_to_display.items()):
        print(f"{k:<3}: {v}")


def alphabet_not_in_text(text):
    """
    Receives a string. Returns a sorted list of chars from alphabet that are not in text.
    Ignores case. Uses set functionality
    """
    set_letter_not_in_text = set(string.ascii_lowercase) - set(text.lower())

    list_letters_not_in_text = list(sorted(set_letter_not_in_text))

    return list_letters_not_in_text


# Test 1
test_text_1 = input("Enter a text: ")
if len(test_text_1) == 0:
    test_text_1 = "Mama Myla RaMU PaPU bilI V RyLo VesLom"

unique_letters = get_unique_chars(test_text_1)
display_sorted_dictionary_two_cols(unique_letters)
print(alphabet_not_in_text(test_text_1))


# Test 2 - answer to challenge is ['q', 'z']
test_text_2 = input("Enter a text: ")
if len(test_text_2) == 0:
    test_text_2 = "abc DEF GHI JKLMno PRsTUvwxy ABC DEF GHIJKLMNOPRTYSVSVS RRTS VV"

unique_letters = get_unique_chars(test_text_2)
display_sorted_dictionary_two_cols(unique_letters)
print(alphabet_not_in_text(test_text_2))
