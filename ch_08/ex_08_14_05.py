# Exercise 08_14_05 from Deitel: Intro to Python and CS

"""
Reimplement Exercises 8.5 using regular expressions that capture the matching substrings, then display them.

Exercise 08_05:
Write a script that reads a line of text,
tokenizes the line using space characters as delimiters and outputs only those words beginning with the letter 'a'.
"""

import numpy as np
import pandas as pd
import random
import re


def print_all_words_containing_char(text, char='b'):
    """
    Prints in one line all words from a string (text) containing specified char ("b" by default)
    :param text: String containing lowercase words separated by space
    :param char: One char, type str
    :return: None (prints corresponding words in one line)
    """
    # Split text into a list of individual words using findall
    split_text = re.findall(r"(\w+)", text)
    # Iterate over the list of individual words and print word if it contains  (char)
    for word in split_text:
        if re.fullmatch(r"\w*{}\w*".format(char), word):
            print(word, end=" ")
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
arr_prepos = np.array(['on', 'to', 'upon', 'about', 'in', 'after', 'against', 'upon'])

# Generate and print 20 sentences as well as all words containing "a"
for i in range(20):
    # Generate and print original sentence
    input_sentence = generate_sentence(arr_nouns, arr_verbs, arr_prepos)
    print("Original: ")
    print(input_sentence)

    # Announce printing words that start with "a"
    print("Words containing with a:")
    # Display words starting with "a"
    print_all_words_containing_char(text=input_sentence, char="a")

    # Print separator
    print("----------------------------")
