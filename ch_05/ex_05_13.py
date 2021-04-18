"""
Produce the possible phone number for the given seven-letter string.
"""
import string


def get_string_from_user(wanted_length: int = 7):
    """
    Gets string from user of specified length. Default is 7.
    Checks: length 7 and only chars except q and z. Prompts for new input if wrong format.
    :return: String as str.
    """
    entered_string = input(f"Enter your {wanted_length}-letter word: ")
    entered_correctly = False
    while not entered_correctly:
        # Check length
        if len(entered_string) != wanted_length:
            print(f"Word must contain exactly {wanted_length} letters. Please try again.")
            entered_string = input(f"Enter your {wanted_length}-letter word: ")
            continue
        # After that check for only lowercase letters
        elif any([True for x in entered_string if x not in string.ascii_lowercase]):
            print("Word must consist of lowercase letters only. Please try again.")
            entered_string = input(f"Enter your {wanted_length}-letter word: ")
            continue
        # After that check for absence of "q" and "z"
        elif "q" in entered_string or "z" in entered_string:
            print(f"Word may not contain q or z. Please try again.")
            entered_string = input(f"Enter your {wanted_length}-letter word: ")
            continue
        else:
            entered_correctly = True
    return entered_string


def gen_phone_number(word: str, dict_chars_to_nums: dict):
    """
    Receives word as a string and dictionary mapping chars to digits. Returns corresponding phone number as string
    :param word: Word from user that need to be mapped to digits
    :param dict_chars_to_nums: Dictionary with digits 2 to 9 as keys and tuples of 3 corresponding letters as values
    :return: A phone number as string
    """
    # Empty string to hold the generated phone number
    phone_num_str = ""

    # Convert chars from word to digits and append to phone_num_str
    for char in word:
        for key, value in dict_chars_to_nums.items():
            if char in key:
                phone_num_str += str(value)

    return phone_num_str


# Define dictionary with numbers to letters correspondence
digit_to_letters_dict = {2: ("a", "b", "c"), 3: ("d", "e", "f"), 4: ("g", "h", "i"), 5: ("j", "k", "l"),
                         6: ("m", "n", "o"), 7: ("p", "r", "s"), 8: ("t", "u", "v"), 9: ("w", "x", "y")}

# Define dictionary with letter to numbers correspondence
letter_to_digit_dict = {value: key for key, value in digit_to_letters_dict.items()}

# Get string from user
word_from_user = get_string_from_user()

# Generate possible phone number
good_phone_number = gen_phone_number(word_from_user, letter_to_digit_dict)

if len(good_phone_number) == 7:
    print(f"Phone number corresponding to your word is: {good_phone_number[:3]}-{good_phone_number[3:5]}"
          f"-{good_phone_number[5:]}")
else:
    print(good_phone_number)
