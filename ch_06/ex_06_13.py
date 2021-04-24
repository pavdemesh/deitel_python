# Exercise 06_12 from Deitel: Intro to Python for CS
"""
Use an online thesaurus to look up synonyms for five words.
Create a synonyms dictionary that maps those words to lists containing three synonyms for each word.
Display the dictionary’s contents as a key with an indented list  of synonyms below it.
"""

synonyms = dict()
synonyms.update(brave=['heroic', 'courageous', 'daring'], smart=['clever', 'genius', 'brainy'],
                understand=['know', 'apprehend', 'grasp'], house=['building', 'condo', 'dwelling'],
                repeat=['rerun', 'replay', 'reiterate'])

for word, list_of_syns in sorted(synonyms.items()):
    print(f"{word:>11}:", *[f"{x:<12}" for x in list_of_syns])
