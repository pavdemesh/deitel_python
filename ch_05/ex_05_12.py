"""
Given a seven-digit number, 
generate every possible seven-letter word combination corresponding to that number. 
There are 2,187 (37) such combinations.
Avoid phone numbers with the digits 0 and 1 (to which no letters correspond). 
See 6if your phone number corresponds to meaningful words and display those.
"""


def get_phone_from_user(number_length: int = 7):
    """
    Gets phone number from user of specified length. Default is 7.
    Checks: length 7 and digits 2 through 9 only. Prompts for new input if wrong format.
    :return: Phone number as string.
    """
    number = input("Enter your 7-digit phone number: ")
    entered_correct_phone = False
    while not entered_correct_phone:
        if len(number) != number_length:
            print(f"Number must contain {number_length} digits. Please try again.")
            number = input(f"Enter your {number_length}-digit phone number: ")
            continue
        elif any([True for x in number if x not in '23456789']):
            print("Number must consist of digits 2 through 9 only. Please try again.")
            number = input(f"Enter your {number_length}-digit phone number: ")
            continue
        else:
            entered_correct_phone = True
    return number


def get_legit_words(txt_file: str = "words.txt", desired_length: int = 7):
    """
    Returns a list of words of required length based on dictionary provided as 1st argument.
    Legit words have no apostrophes or digits in them but may contain dashes.
    Legit words also do not contain z and q (not present on phone buttons).
    :param txt_file: Name of an txt dictionary file containing one word per line. Default is "words.txt".
    :param desired_length: Words of what length must be returned. Default is 7.
    :return: List containing words of desired_length from txt dictionary
    """
    fh = open(txt_file, "r")  # words.txt  must be located in the same folder as the script

    # Create empty list to store legit words
    legit_words = []

    # Iterate over txt dictionary file line by line and append to legit_words if the word is legit
    for word in fh:
        word = word.lower().strip()
        mytable = word.maketrans("y", "y", "-")

        # Filter out words of length other than 7
        if len(word.translate(mytable)) == desired_length:
            # Additional check for words of desired_length: must consist only of chars except q and z plus dash
            is_legit = True
            for char in word:
                if char not in "abcdefghijklmnoprstuvwxy-":
                    is_legit = False
                    break
            if is_legit:
                legit_words.append(word)

    return legit_words


def gen_possible_combinations(number: str, dict_nums_chars: dict):
    """
    Receives phone number and mapping of digits to chars as input and returns possible 7-letter combinations
    :param number: Phone number as int of len 7
    :param dict_nums_chars: Dictionary with digits 2 to 9 as keys and tuples of 3 corresponding letters as values
    :return: A list of lowercase strings: possible 7-letter combinations
    """
    possible_combinations = list()
    # Convert phone number to str to access individual letters
    for i in dict_nums_chars[int(number[0])]:
        for j in dict_nums_chars[int(number[1])]:
            for k in dict_nums_chars[int(number[2])]:
                for s in dict_nums_chars[int(number[3])]:
                    for m in dict_nums_chars[int(number[4])]:
                        for n in dict_nums_chars[int(number[5])]:
                            for p in dict_nums_chars[int(number[6])]:
                                possible_combinations.append((i + j + k + s + m + n + p).lower())
    return possible_combinations


def find_memorizable_words(list_of_strings, dictionary):
    """
    Receives list of strings and dictionary
    Returns words from list_of_words also contained in dictionary
    """
    memorizable_words = list()
    for lexeme in dictionary:
        mytable = lexeme.maketrans("y", "y", "-")
        if lexeme.translate(mytable) in list_of_strings:
            memorizable_words.append(lexeme.translate(mytable).upper())
    return memorizable_words


# Define dictionary with numbers to letters correspondence
digit_to_letters_dict = {2: ("a", "b", "c"), 3: ("d", "e", "f"), 4: ("g", "h", "i"), 5: ("j", "k", "l"),
                         6: ("m", "n", "o"), 7: ("p", "r", "s"), 8: ("t", "u", "v"), 9: ("w", "x", "y")}

# Get phone number from user
phone_num = get_phone_from_user()

# Load words from dictionary and put all words of desired_length in separate list
all_good_words = get_legit_words("words.txt", desired_length=7)

# Generate all possible 7-letter combinations and store them as a list
all_combinations = gen_possible_combinations(phone_num, digit_to_letters_dict)

# Compare generated combinations against dictionary and store memorizing suggestions to a list
memorizing_suggestions = find_memorizable_words(all_combinations, all_good_words)

if memorizing_suggestions:
    print("We suggest following word(s) as memorization help:")
    print(*memorizing_suggestions)
else:
    print("Unfortunately,  there are no feasible memorizing suggestions.")
