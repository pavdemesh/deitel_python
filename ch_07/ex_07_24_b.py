# Exercise 07_24 from Deitel: Intro to Python for CS

"""
Knight’s Tour problem, originally proposed by the mathematician Euler.
Can the knight move around an empty chessboard and touch each of the 64 squares once and only once?

The knight makes only L-shaped moves (two spaces in one direction and one space in a perpendicular direction).

b) Develop a script that will move the knight around a chessboard represented by an 8-by-8 2D array named board.
Initialize each square to zero.
We describe each of the eight possible moves in terms of its horizontal and vertical components. For example:
A move consists of moving two squares horizontally to the right and one square vertically upward.
A move consists of moving one square horizontally to the left and two squares vertically upward.
Horizontal moves to the left and vertical moves upward are indicated with negative numbers.
The eight moves may be described by two one-dimensional arrays, horizontal and vertical, as follows:
horizontal[0] = 2 vertical[0] = -1
horizontal[1] = 1 vertical[1] = -2
horizontal[2] = -1 vertical[2] = -2
horizontal[3] = -2 vertical[3] = -1
horizontal[4] = -2 vertical[4] = 1
horizontal[5] = -1 vertical[5] = 2
horizontal[6] = 1 vertical[6] = 2
horizontal[7] = 2 vertical[7] = 1

Variables current_row and current_column indicate the row and column, respectively, of the knight’s current position.
To make a move of type move_number (a value 0–7), your script should use the statements:
current_row += vertical[move_number]
current_column += horizontal[move_number]

Write a script to move the knight around the chessboard. Keep a counter that varies from 1 to 64.
Record the latest count in each square the knight moves to.
Test each potential move to see if the knight has already visited that square.
Test every potential move to ensure that the knight does not land off the chessboard.
Run the application. How many moves did the knight make?
"""

import numpy as np
import random


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
    print(f"Starting Knight's Tour at position: [{current_row}][{current_col}]")

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

    print(f"Tour ended on move #: {count_moves}")
    print("The chessboard after Knight's Tour looks as follows:")
    print(chessboard)


run_knights_tour()
