# Exercise 08_11 from Deitel: Intro to Python and CS

"""
Write a script that enables the user to enter mathematical word problems like “two times three” and “seven minus five”.
Then use string processing to break apart the string into the numbers and the operation and return the result.
So “two times three” would return 6 and “seven minus five” would return 2.
To keep things simple, assume the user enters only the words for the numbers 0 through 9
and only the operations 'plus', 'minus', 'times' and 'divided by'.
"""

# Dictionary of operations
math_operations = {'minus': '-', 'plus': '+', 'times': '*', 'divided by': '/'}

# Dictionary to map word numbers to digits
words_to_numbers = {'zero': '0', 'one': '1', 'two': '2', "three": "3", "four": "4", "five": "5", "six": "6",
                    "seven": "7", "eight": "8", "nine": "9"}

# Get input
word_problem = input()

# Split input into separate words
word_problem_split = word_problem.split()

# If three words - assign left, operator, right
if len(word_problem_split) == 3:
    left_operand, operator, right_operand = word_problem_split
# Else, len == 4 and operation is divided by and operator consists of second and third word
else:
    left_operand, operator, right_operand = word_problem_split[0], " ".join(word_problem_split[1:3]), \
                                            word_problem_split[3]

# Calculate the result
result = eval(words_to_numbers[left_operand] + math_operations[operator] + words_to_numbers[right_operand])

# Display result
print(result)
