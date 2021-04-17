"""
Given a seven-digit number, 
generate every possible seven-letter word combination corresponding to that number. 
There are 2,187 (37) such combinations.
Avoid phone numbers with the digits 0 and 1 (to which no letters correspond). 
See 6if your phone number corresponds to meaningful words and display those.
"""


import string

fh = open("words.txt", "r")  # words.txt  must be located in the same folder as the script

# Create empty list to store legit 7 letters words without numbers, punctuation and dashes and without "q" and "z"
legitimate_words = []

# Iterate over words.txt word by word and append to legitimate_words if the word is legit
for word in fh:
    word = word.lower().strip()
    if len(word) != 7:
        continue
    else:
        is_legit = True
        for char in word:
            if char not in string.ascii_lowercase:
                is_legit = False
                break
            elif char == "z" or char == "q":
                is_legit = False
                break
        if is_legit:
            legitimate_words.append(word)
# List legitimate_words now contains all 7 letters long legit words

# Define e dictionary with numbers to letters correspondence
number_to_letters_dict = {2: ("A", "B", "C"), 3: ("D", "E", "F"), 4: ("G", "H", "I"), 5: ("J", "K", "L"),
                          6: ("M", "N", "O"), 7: ("P", "R", "S"), 8: ("T", "U", "V"), 9: ("W", "X", "Y")}


def generate_letter_combinations(phone_number: int, dict_nums_chars: dict):
    """
    Receives phone number and mapping of digits to chars as input and returns possible 7-letter combinations
    :param phone_number: Phone number as int of len 7
    :param dict_nums_chars: Dictionary with digits 2 to 9 as keys and tuples of 3 corresponding letters as values
    :return: A list of lowercase strings: possible 7-letter combinations
    """
    possible_combinations = list()
    # Convert phone number to str to access individual letters
    phone_number = str(phone_number)
    for i in dict_nums_chars[int(phone_number[0])]:
        for j in dict_nums_chars[int(phone_number[1])]:
            for k in dict_nums_chars[int(phone_number[2])]:
                for s in dict_nums_chars[int(phone_number[3])]:
                    for m in dict_nums_chars[int(phone_number[4])]:
                        for n in dict_nums_chars[int(phone_number[5])]:
                            for p in dict_nums_chars[int(phone_number[6])]:
                                possible_combinations.append((i + j + k + s + m + n + p).lower())
    return possible_combinations


# Get phone number from user
phone = input("Enter your 7-digit phone number: ")
if len(phone) == 0:
    phone = 6862377
else:
    phone = int(phone)

# Generate all possible 7-letter combinations and store them as a list
generated_combinations = generate_letter_combinations(phone, number_to_letters_dict)


def find_legit_words(list_of_strings, dictionary):
    """
    Receives list of strings and dictionary
    Returns words from list_of_words also contained in dictionary
    """
    legit_words = list()
    for lexeme in list_of_strings:
        if lexeme in dictionary:
            legit_words.append(lexeme.upper())
    return legit_words


memorizing_suggestions = find_legit_words(generated_combinations, legitimate_words)

print("We suggest following words as memorization help:")
print(*memorizing_suggestions)
