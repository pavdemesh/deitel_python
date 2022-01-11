# Exercise 09_10 from Deitel: Intro to Python and CS

"""
Create a word cloud that visualizes the top 200 words in Pride and Prejudice.
"""

from wordcloud import WordCloud
import re

# Initialize frequency dictionary for words
freqs_all_words = dict()

# Open file
with open("ex_09_10_pride_full.txt", mode='r', encoding='utf-8') as fh_text:
    for line in fh_text:
        # First cleaning of the line
        line = line.strip()                     # Strip all whitespaces
        line = re.sub(r"_", "", line)           # Remove underscores
        line = re.sub(r"—", " ", line)          # Replace dash with space

        # Remove punctuation such as "", :, ; -
        line = re.sub(r'[)(“,”:;]+', "", line)

        # Split into a list of words
        words_from_line = line.split()

        # Process words in the list by removing 's and ?!.
        for ind, word in enumerate(words_from_line):
            # Remove (?!.)
            if re.fullmatch(r"\w+[?!.]", word):
                words_from_line[ind] = word[:-1]
            if re.fullmatch(r"\w+’s", word):
                words_from_line[ind] = word[:-2]

        # Update words frequencies
        for word in words_from_line:
            freqs_all_words[word] = freqs_all_words.get(word, 0) + 1

freqs_tuples = sorted(freqs_all_words.items(), reverse=True, key=lambda x: x[1])[:100]
frequencies = {k: v for k, v in freqs_tuples}

# Draw a wordcloud
wcloud = WordCloud(colormap='prism', background_color='white')
wcloud = wcloud.fit_words(frequencies)
wcloud = wcloud.to_file("pride.png")
