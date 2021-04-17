import random


def gen_2_ints(difficulty=1):
    """ Generates two random ints with range depending on difficulty level

    Level 1 means ints in range(2, 21)
    Level 2 means ints in range(20, 100)
    Returns: Tuple of two random ints in particular range
    """
    if difficulty == 1:
        num1 = random.randrange(2, 21)
        num2 = random.randrange(2, 21)
    else:
        num1 = random.randrange(20, 100)
        num2 = random.randrange(20, 100)
    return num1, num2


def gen_task(num1, num2, task=3):
    """ Generates task of specific type based on user input

    Task type: 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division
    Arguments: 2 ints as operands followed by an int as task type (3 by default)
    Asks user for inputting the answer
    Returns user_answer and correct_answer as tuple
    """
    if task == 1:
        ans = int(input(f"What is the sum of {num1} and {num2}?: "))
        res = num1 + num2
    elif task == 2:
        ans = int(input(f"How much is {num1} minus {num2}?: "))
        res = num1 - num2
    elif task == 3:
        ans = int(input(f"How much is {int1} times {int2}?: "))
        res = num1 * num2
    else:  # if task == 4
        ans = int(input(f"How much is {int1} divided by {int2}?: "))
        res = num1 // num2

    return ans, res


react_correct = ["Very good!", "Nice work!", "Keep up the  good work!"]
react_wrong = ["Wrong. Try once more.", "No. PLease try again.", "No. Keep trying"]

difficulty_level = int(input("Enter difficulty 1 or 2: "))
task_type = int(input(f"Select task type: 1 for addition, 2 for subtraction, 3 for multiplication, "
                      f"4 for division, 5 for random mixture: "))
current_task = task_type

while True:
    int1, int2 = gen_2_ints(difficulty_level)
    answered_correctly = False
    if task_type == 5:
        current_task = random.randrange(1, 5)
    user_answer, correct_answer = gen_task(int1, int2, current_task)

    if user_answer == correct_answer:
        print(react_correct[random.randrange(3)])
        answered_correctly = True

    while not answered_correctly:
        print(react_wrong[random.randrange(3)])
        user_answer, correct_answer = gen_task(int1, int2, current_task)

        if user_answer == correct_answer:
            answered_correctly = True
            print(react_correct[random.randrange(3)])
