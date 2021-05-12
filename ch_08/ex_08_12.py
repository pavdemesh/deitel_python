# Exercise 08_12 from Deitel: Intro to Python and CS

"""
Use string-processing capabilities to keep the first and last letter of a word
and scramble the remaining letters in between the first and last.
Search online for “University of Cambridge scrambled text” for an intriguing paper on the readability
of texts consisting of such scrambled words.
Investigate the random module’s shuffle function to help you implement this exercise’s solution.
"""

import random

# Get input from user
text = input()

# Split input into separate words and store in a list
text_split = text.split()

# For each word in the list - keep first and last and scramble the middle
for i, word in enumerate(text_split):
    # Check if length of the word is 3 or less, skip if True, else process word
    if len(word) < 4:
        continue
    else:
        # Convert middle to a list of individual chars
        scrambled_middle = list(word[1:-1])
        # Shuffle list of chars
        random.shuffle(scrambled_middle)
        # Join shuffled chars back to one string
        scrambled_middle = "".join(scrambled_middle)
        # Keep first and last and insert new shuffled middle
        text_split[i] = word[0] + scrambled_middle + word[-1]

# Join individual words from the list into a single string
result = " ".join(text_split)

# Display the resulting string
print(result)
