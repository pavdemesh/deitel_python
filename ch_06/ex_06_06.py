"""
Write a function that receives a list of words.
The determines and displays in alphabetical order only the unique words. 
Treat uppercase and lowercase letters the same. 
The function should use a set to get the unique words in the list. 
Test your function with several sentences.
"""


def display_unique_words(words_list):
    """
    Receives a list of words as input. Case insensitive.
    Returns a set of unique words. 
    Prints the set in alphabetical order.
    """
    unique_words = set(word.lower() for word in words_list)

    for item in sorted(unique_words):
        print(item)

    return unique_words


# Test 1 - Test if the function produces correct set of unique lowercase words
input_test_1 = list("Mama Ramu MAMA MYLa RAmu maMa raMu myLa".split())
correct_output_test_1 = {'mama', 'ramu', 'myla'}
answer_test_1 = display_unique_words(input_test_1)

if answer_test_1 == correct_output_test_1:
    print("Test 1 passed successfully.")


# Test 2 - Test if the technique used in func() for alphabetical printing of set's items is correct
input_test_2 = list("Mama Ramu MAMA MYLa RAmu maMa raMu myLa".split())
correct_output_test_2 = ['mama', 'myla', 'ramu']
answer_test_2 = list()
# Use the logic for alphabetical printing to append words from set to a list in alphabetical order.
for word in sorted(display_unique_words(input_test_1)):
    answer_test_2.append(word)

if answer_test_2 == correct_output_test_2:
    print("Test 2 passed successfully.")
