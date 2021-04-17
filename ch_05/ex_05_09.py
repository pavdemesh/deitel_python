import string


def is_palindrome(sequence):
    """
    Takes a string and returns True if it’s a palindrome and False otherwise.
    Uses a stack (simulated with a list) to help determine whether a string is a palindrome.
    Ignore case sensitivity, spaces and punctuation.
    """
    # Create a list, populate with letters from original string igrnoring spaces and punctuation
    list_original = list()
    for char in sequence:
        if char.lower() in string.ascii_lowercase:
            list_original.append(char.lower())
    
    # Create reversed list
    list_reversed = list(reversed(list_original))
    
    # Compare element by element using pop()
    # Return False if elements are not the same
    for i in range(len(list_original) // 2 + 1):
        if list_original.pop() != list_reversed.pop():
            return False
    
    return True
    

test1 = "! aB, cd ef@@f Ed cba"             # "abcdeffedcba"
test2 = "AB^^CDE::FFyE $$ DC!!!BA    "      # "abcdeff-y-edcba"

print(is_palindrome(test1))
print(is_palindrome(test2))
