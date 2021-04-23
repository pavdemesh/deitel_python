"""
Write a script:
that uses a dictionary to determine and print the number of duplicate words in a sentence. 
Treat uppercase and lowercase letters the same and assume there is no punctuation in the sentence.
Use the techniques you learned in Section 6.2.7. 
Words with counts larger than 1 have duplicates.
"""

def find_duplicates(text):
    """
    Receives a string as input and returns a list of duplicate words from that string AND
    the total number of duplicates.
    IMPORTANT: Input string must not contain punctuation!
    Lowercase and uppercase insensitive, i.e. treats as same words.
    """
    # Dictionary to store unique words and their counts
    unique_words = {}
    for word in list(text.lower().split()):
        unique_words[word] = unique_words.get(word, 0) + 1

    # List to hold duplicates
    duplicates = list()
    for word, frequency in unique_words.items():
        if frequency > 1:
            duplicates.append(word)

    # Determine total number of duplicates: subtract the total count of unique words from total count of all words
    total_count_duplicates = len(text.split()) - len(unique_words)

    return duplicates, total_count_duplicates


test = "mama Mama myla ramu ramU MaMa myLA Myla mama pilorama"
repetitions_list, repetitions_count = find_duplicates(test)

print(repetitions_count)
print(repetitions_list)
