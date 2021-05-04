# Exercise 07_25 from Deitel: Intro to Python for CS

"""
Knight’s Tour problem, originally proposed by the mathematician Euler.
Can the knight move around an empty chessboard and touch each of the 64 squares once and only once?

The knight makes only L-shaped moves (two spaces in one direction and one space in a perpendicular direction).

a) Use random-number generation to enable the knight to walk around the chessboard
(in its legitimate L-shaped moves) at random.
Your script should run one tour and display the final chessboard. How far did the knight get?

b) Most likely, the script in Part (a) produced a relatively short tour.
Now modify your script to attempt 1,000,000 tours.
Use a one-dimensional array to keep track of the number of tours of each length.
When your script finishes attempting the 1,000,000 tours, it should display this information in a neat tabular format.
What was the best result?

c) Most likely, the script in Part (b) gave you some “respectable” tours, but no full tours.
Now let your script run until it produces a full tour.
[Caution: This version of the script could run for hours on a powerful computer.]
Once again, keep a table of the number of tours of each length,
and display this table when the first full tour is found.
How many tours did your script attempt before producing a full tour? How much time did it take?
"""

import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns


def draw_board(size=8, filler=0):
    """
    Creates 2D ndarray of given size filled with specified filler value
    :param size: Int, array will be 2D in form size-by-size (8-by-8 default)
    :param filler: Int, array will be filled with this filler (0 is default)
    :return: 2D ndarray
    """
    board = np.full((size, size), filler)
    return board


def is_valid_move(curr_row, curr_col, row_shift, col_shift, board, filler=0):
    """
    Checks whether the given move of the knight would be a valid move (empty target + within borders)
    :param curr_row: Int, current row position
    :param curr_col: Int, current column position
    :param row_shift: Vertical change of current position (possible values would be -1, -2, 1, 2)
    :param col_shift: Horizontal change of current position (possible values would be -1, -2, 1, 2)
    :param board: 2D ndarray
    :param filler: Int, filler signalling that the target square is still empty
    :return: True if valid move else False
    """
    # Check that the move would be within the size of the border
    lower_border = 0
    upper_border = board.shape[0] - 1
    if curr_row + row_shift < lower_border or curr_row + row_shift > upper_border:
        return False
    if curr_col + col_shift < lower_border or curr_col + col_shift > upper_border:
        return False

    # Check that the targeted square is empty
    if board[curr_row + row_shift][curr_col + col_shift] != filler:
        return False
    # If both tests successfully passed, return True
    return True


def get_all_valid_moves(curr_row, curr_col, board, filler=0):
    """
    Returns a list of valid moves each as tuple containing row_shift and col_shift
    :param curr_row: Int, current row position
    :param curr_col: Int, current column position
    :param board: 2D ndarray
    :param filler: Int, filler signalling that the target square is still empty
    :return: List of all valid moves each as tuple containing row_shift and col_shift
    """
    # Create empty list to store valid moves
    valid_moves = list()

    # Iterate over all possible moves
    row_shifts = np.array([1, 2, -1, -2, 1, 2, -1, -2])
    col_shifts = np.array([2, 1, 2, 1, -2, -1, -2, -1])

    for i in range(8):
        row_step = row_shifts[i]
        col_step = col_shifts[i]
        if is_valid_move(curr_row, curr_col, row_step, col_step, board, filler):
            valid_moves.append((row_step, col_step))

    return valid_moves


def pick_first_move_from_list(arr):
    """
    Returns first element from the list
    :param arr: List of items
    :return: First element (index[0])
    """
    return arr[0]


def pick_random_move_from_list(arr):
    """
    Returns random element from list
    :param arr: List of items
    :return: Randomly picked element from list
    """
    return arr[random.randrange(0, len(arr))]


def run_knights_tour():
    """
    Run Knight's Tour on an 8-by-8 board
    :return: Count of the last move made by Knight
    """
    # Initialize chessboard
    chessboard = draw_board()

    # Initialize variables to hold position of the knight
    current_row = random.randint(0, 7)
    current_col = random.randint(0, 7)

    # Display initial position of the Knight
    # print(f"Starting Knight's Tour at position: [{current_row}][{current_col}]")

    # Counter for moves done by knight (initial value is 1, starting position of the knight)
    count_moves = 1

    # Initialize flag to control whether the Knight can move at all
    knight_can_move = True

    # Repeat while the knight can move:
    while knight_can_move:
        chessboard[current_row][current_col] = count_moves
        # Get the list of possible moves
        possible_moves = get_all_valid_moves(current_row, current_col, chessboard)

        # If no possible move: stop tour and return count of moves made
        if len(possible_moves) == 0:
            knight_can_move = False
            continue
        # Else pick one move from possible moves and update position of Knight and count of moves
        else:
            vertical_shift, horizontal_shift = pick_random_move_from_list(possible_moves)
            current_row += vertical_shift
            current_col += horizontal_shift
            count_moves += 1

    return count_moves


# c) Run script for 10_000 times
tours_results = np.full(65, 0)
for i in range(1_000_000):
    last_move = run_knights_tour()
    tours_results[last_move] += 1
    if i % 5000 == 0:
        print(str(i).zfill(7))

# Visualize results
tour_length_freqs = {i: tours_results[i] for i in range(65) if tours_results[i] > 0}
# print(tour_length_freqs)

sns.set_style(style='whitegrid')
my_plot = sns.barplot(x=list(tour_length_freqs.keys()), y=list(tour_length_freqs.values()))
plt.xticks(rotation='vertical')
my_plot.tick_params(labelsize=8)
plt.show()
