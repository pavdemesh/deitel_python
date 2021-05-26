# Exercise 09_10 from Deitel: Intro to Python and CS

"""
A great source of plain text files is the collection of over 57,000 free e-books at Project Gutenberg.

Download the text-file version of Pride and Prejudice from Project Gutenberg
https://www.gutenberg.org/ebooks/1342

Create a script that reads Pride and Prejudice from a text file.
Produce statistics about the book, including the total word count, the total character count, the average word length,
the average sentence length, a word distribution containing frequency counts of all words, and the top 10 longest words.

Each Project Gutenberg e-book begins and ends with some additional text, such as licensing information,
which is not part of the e-book itself.
You may want to remove that text from your copy of the book before analyzing its text.
"""

import re

# Initialize frequency dictionary for words
freqs_all_words = dict()

# Initialize counters for chars
total_chars_with_spaces = 0
total_chars_without_spaces = 0

# Initialize counters for sentences
cur_sent_len = 0
total_sent_len = 0
total_sent_count = 0

# Open file
with open("ex_09_10_pride_full.txt", mode='r', encoding='utf-8') as fh_text:
    for line in fh_text:
        # First cleaning of the line
        line = line.strip()                     # Strip all whitespaces
        line = re.sub(r"_", "", line)           # Remove underscores
        line = re.sub(r"—", " ", line)          # Replace dash with space
        # Iterate over line char-by-char and update chars counters
        for char in line:
            if char == " ":
                total_chars_with_spaces += 1
            else:
                total_chars_with_spaces += 1
                total_chars_without_spaces += 1

        # Remove punctuation such as "", :, ; -
        line = re.sub(r'[)(“,”:;]+', "", line)

        # Split into a list of words
        words_from_line = line.split()

        # Count sentence stats
        for word in words_from_line:
            # If the word ends with ? or ! or . (not preceded by Mr or Mrs): end of sentence
            if re.fullmatch(r"\w+[?!]|\w+(?<!Mr)[.]|\w+(?<!Mrs)[.]", word):
                cur_sent_len += 1
                total_sent_len += cur_sent_len
                total_sent_count += 1
                cur_sent_len = 0
            else:
                cur_sent_len += 1

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

# Display results for chars statistics
print(f"Total characters count with spaces is: {total_chars_with_spaces:,} chars")
print(f"Total characters count without spaces is: {total_chars_without_spaces:,} chars")

# Display results for sentence statistics:
print(f"Total sentences count is: {total_sent_count:,} sentences")
print(f"Average sentence length is: {total_sent_len / total_sent_count:.1f} words")

# Display results for word statistics
total_words_length = sum(len(key) * num for key, num in freqs_all_words.items())
total_words_count = sum(freqs_all_words.values())
print(f"Average word length is: {total_words_length / total_words_count:.1f} chars")

print(f"Top ten longest words are:")
longest_words = sorted(freqs_all_words, reverse=True, key=lambda x: len(x))[:10]
for word in longest_words:
    print(f"Word '{word}' has {len(word)} characters")
