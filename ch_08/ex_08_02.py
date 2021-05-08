# Exercise 08_02 from Deitel: Intro to Python and CS

"""
Write a script that uses random-number generation to compose sentences.

Use four arrays of strings called article, noun, verb and preposition.
Create a sentence by selecting a word at random from each array in the following order:
article, noun, verb, preposition, article and noun.
As each word is picked, concatenate it to the previous words in the sentence.
Spaces should separate the words.
When the final sentence is output, it should start with a capital letter and end with a period.
The script should generate and display 20 sentences.
"""

import numpy as np
import pandas as pd
import random


def generate_sentence(articles, nouns, verbs, prepositions):
    """
    Return a randomly generated string based on four arrays> articles, nouns, verbs, prepositions.
    The resulting sentence has form: Article + noun + verb + preposition + article.
    :param articles: Array containing English articles as strings
    :param nouns: Array containing English nouns as strings
    :param verbs: Array containing English verbs as strings
    :param prepositions: Array containing English prepositions as strings
    :return: String
    """
    # Select noun1
    noun1 = nouns[random.randrange(nouns.size)]

    # Select article1 choosing correctly between "a" and "an"
    noun1_needs_an = noun1[0] in 'aeiou'
    if noun1_needs_an:
        article1 = articles[random.randrange(1, 3)]
    else:
        article1 = articles[random.randrange(0, 3, 2)]

    # Select verb1
    verb1 = verbs[random.randrange(verbs.size)]

    # Select preposition1
    prepos1 = prepositions[random.randrange(prepositions.size)]

    # Select noun2
    noun2 = nouns[random.randrange(nouns.size)]

    # Select article2 choosing correctly between "a" and "an"
    noun2_needs_an = noun2[0] in 'aeiou'
    if noun2_needs_an:
        article2 = articles[random.randrange(1, 3)]
    else:
        article2 = articles[random.randrange(0, 3, 2)]

    # Return result
    return " ".join([article1.capitalize(), noun1, verb1, prepos1, article2, noun2]) + "."


# Array of articles
arr_articles = np.array(['a', 'an', 'the'])

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
arr_prepos = np.array(['on', 'to', 'upon', 'about', 'in', 'after', 'against'])

# Generate and print 20 sentences
for i in range(20):
    print(generate_sentence(arr_articles, arr_nouns, arr_verbs, arr_prepos))
