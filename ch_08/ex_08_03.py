# Exercise 08_03 from Deitel: Intro to Python and CS

"""
Write a script that encodes English-language phrases into a form of coded language called pig Latin.

For simplicity, use the following algorithm:
To form a pig Latin phrase from an English-language phrase, tokenize the phrase into words with string method split.
To translate each English word into a pig Latin word,
place the first letter of the English word at the end of the word and add the letters “ay.”
Thus, the word “jump” becomes “umpjay,” the word “the” becomes “hetay,” and the word “computer” becomes “omputercay.”
If the word starts with a vowel, just add “ay.”
Blanks between words remain as blanks.

Assume the following: The English phrase consists of words separated by blanks,
there are no punctuation marks and all words have two or more letters.
Enable the user to enter a sentence, then display the sentence in pig Latin.
"""

import numpy as np
import pandas as pd
import random


def generate_pig_latin(text):
    """
    Generates a pig Latin phrase based on a given phrase
    :param text: String
    :return: Encoded string
    """
    words = text.split()
    pig_latin_words = []
    for word in words:
        if word[0] in  'aeiou':
            pig_latin_words.append(word + "ay")
        else:
            pig_latin_words.append(word[1:] + word[0] + "ay")

    return " ".join(pig_latin_words)


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

# Generate and print 5 sentences and their equivalents in pig Latin
for i in range(20):
    sentence_english = generate_sentence(arr_nouns, arr_verbs, arr_prepos)
    print(sentence_english)
    sentence_pig_latin = generate_pig_latin(sentence_english)
    print(sentence_pig_latin)
