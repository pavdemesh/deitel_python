# Exercise 08_06 from Deitel: Intro to Python and CS

"""
Write a script that reads a line of text,
tokenizes it using space characters as delimiters and outputs only those words ending with the letters 'ed'.
"""

import numpy as np
import pandas as pd
import random


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

# Generate and print 20 sentences and words containing "a"
for i in range(20):
    # Generate and print original sentence
    input_sentence = generate_sentence(arr_nouns, arr_verbs, arr_prepos)
    print("Original: ")
    print(input_sentence)
    # Announce printing words that end with "er"
    print("Words ending with er:")
    # Display words ending with "er"
    print(" ".join([word for word in input_sentence.split() if word.endswith('er')]))
    # Print separator
    print("----------------------------")
