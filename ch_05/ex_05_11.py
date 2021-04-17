import string


def summarize_letters(seq):
    """
    Receives a string and returns a list of tuples 
    containing the unique letters and their frequencies in the string. 
    Ignores case sensitivity, spaces and punctuation.
    """
    #Create list to hold unique chars with frequencies
    unique_chars_with_frequency = list()
    
    #Make a lower case copy of the input seq
    low_case_seq_copy = seq.lower()
    
    for char in string.ascii_lowercase:
        if char in low_case_seq_copy:
            unique_chars_with_frequency.append((char, low_case_seq_copy.count(char)))
            
    return unique_chars_with_frequency
    
    
test_case_1 = "mama mila ramu papu bili v rylo"
test_case_2 = "namaha    fjsdafja ,,, !!! sjdhfabcdefghijklmnoprsqtuvwxyzabcdefghzyxxzzz"

print(summarize_letters(test_case_1))
print(summarize_letters(test_case_2))


def has_all_alphabet(seq):
    """
    Says whether the string has all the letters of the alphabet.
    """
    return len(summarize_letters(seq)) == 26
    

print(has_all_alphabet(test_case_1))    # False
print(has_all_alphabet(test_case_2))    # True
