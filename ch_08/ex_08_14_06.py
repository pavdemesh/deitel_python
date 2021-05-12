# Exercise 08_14_06 from Deitel: Intro to Python and CS

"""
Reimplement Exercises 8.6 using regular expressions that capture the matching substrings, then display them.

Exercise 08_06:
Write a script that reads a line of text,
tokenizes it using space characters as delimiters and outputs only those words ending with the letters 'ed'.
"""

import numpy as np
import pandas as pd
import random
import re


def print_all_words_ending_with(text, ending="er"):
    """
    Prints in one line all words from a string (text) ending with specified char(s) ("ed" by default)
    :param text: String containing lowercase words separated by space
    :param ending: Chars to be found at the end of each word, type str
    :return: None (prints corresponding words in one line)
    """
    # Slit the text into individual words and iterate over them, checking for required ending:
    for word in re.finditer(r"\w+{}[ \n]".format(ending), text):
        print(word.group(), end=" ")
    print()


def generate_sentence(nouns, verbs, prepositions):
    """
    Return a randomly generated string based on 3 arrays: nouns, verbs, prepositions.
    The resulting sentence has form: Article + noun + verb + preposition + article.
    :param nouns: Array containing English nouns as strings
    :param verbs: Array containing English verbs as strings
    :param prepositions: Array containing English prepositions as strings
    :return: String
    """
    # Select noun1
    noun1 = nouns[random.randrange(nouns.size)]

    # Select verb1
    verb1 = verbs[random.randrange(verbs.size)]

    # Select preposition1
    prepos1 = prepositions[random.randrange(prepositions.size)]

    # Select noun2
    noun2 = nouns[random.randrange(nouns.size)]

    # Select preposition2
    prepos2 = prepositions[random.randrange(prepositions.size)]

    # Select noun3
    noun3 = nouns[random.randrange(nouns.size)]

    # Return result
    return " ".join([noun1, verb1, prepos1, noun2, prepos2, noun3])


# Array of nouns
arr_nouns = np.array(['time', 'year', 'people', 'way', 'day', 'man', 'thing', 'woman', 'life', 'child', 'world',
                      'school', 'state', 'family', 'student', 'group', 'country', 'problem', 'hand', 'part', 'place',
                      'case', 'week', 'company', 'system', 'program', 'question', 'work', 'government', 'number',
                      'night', 'point', 'home', 'water', 'room', 'mother', 'area', 'money', 'story', 'fact', 'month',
                      'lot', 'right', 'study', 'book', 'eye', 'job', 'word', 'business', 'issue', 'side', 'kind',
                      'head', 'house', 'service', 'friend', 'father', 'power', 'hour', 'game', 'line', 'end',
                      'member', 'law', 'car', 'city', 'community', 'name', '', 'president', 'team', 'minute', 'idea',
                      'kid', 'body', 'information', 'back', 'parent', 'face', 'others', 'level', 'office', 'door',
                      'health', 'person', 'art', 'war', 'history', 'party', 'result', 'change', 'morning', 'reason',
                      'research', 'girl', 'guy', 'moment', 'air', 'teacher', 'force', 'education'])

# Array of verbs via import from txt file
verbs_source = pd.read_csv("ex_08_02_verbs.txt", sep="\t", names=["Infin", "Past ", "Perfect", "3rd Person", "Gerund"])
arr_verbs = np.array(verbs_source["3rd Person"])

# Array of prepositions
arr_prepos = np.array(['on', 'to', 'upon', 'about', 'in', 'after', 'against', 'upon', 'ahead of'])

ending_to_find = 'e'

# Generate and print 20 sentences as well as words ending with ending_to_find
for i in range(20):
    # Generate and print original sentence
    input_sentence = generate_sentence(arr_nouns, arr_verbs, arr_prepos)
    print("Original: ")
    print(input_sentence)

    # Announce printing words that end with ending_to_find
    print(f"Words ending with {ending_to_find}:")
    # Display words ending with ending_to_find
    print_all_words_ending_with(input_sentence, ending=ending_to_find)
    # Print separator
    print("----------------------------")
