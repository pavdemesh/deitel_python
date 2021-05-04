# Exercise 07_24_c from Deitel: Intro to Python for CS

"""
Knight’s Tour problem, originally proposed by the mathematician Euler.
Can the knight move around an empty chessboard and touch each of the 64 squares once and only once?

The knight makes only L-shaped moves (two spaces in one direction and one space in a perpendicular direction).

c) You may have observed that the outer squares are more troublesome than the squares nearer the center of the board.
In fact, the most troublesome or inaccessible squares are the four corners.

Intuition may suggest that you should attempt to move the knight to the most troublesome squares first
and leave open those that are easiest to get to so that when the board gets congested near the end of the tour,
there will be a greater chance of success.

We could develop an “accessibility heuristic” by classifying each of the squares according to how accessible it is
and always moving the knight (using the knight’s L-shaped moves) to the most inaccessible square.

We fill two-dimensional array accessibility with numbers
indicating from how many squares each particular square is accessible.
On a blank chessboard, each of the 16 squares nearest the center is rated as 8, each corner square is rated as 2,
and  the other squares have accessibility numbers of 3, 4 or 6 as follows:

2 3 4 4 4 4 3 2
3 4 6 6 6 6 4 3
4 6 8 8 8 8 6 4
4 6 8 8 8 8 6 4
4 6 8 8 8 8 6 4
4 6 8 8 8 8 6 4
3 4 6 6 6 6 4 3
2 3 4 4 4 4 3 2

Write a new version of the Knight’s Tour, using the accessibility heuristic.
The knight should always move to the square with the lowest accessibility number.
In case of a tie, the knight may move to any of the tied squares.
Therefore, the tour may begin in any of the four corners.

[Note: As the knight moves around the chessboard,
your application should reduce the accessibility numbers as more squares become occupied.
In this way, at any given time during the tour, each available square’s accessibility number will remain equal
to precisely the number of squares from which that square may be reached.]
Run this version of your script.
Did you get a full tour? Modify the script to run 64 tours, one starting from each square of the chessboard.
How many full tours did you get?
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


def draw_accessibility():
    """
    Draw an 8-by-8 ndarray with numbers representing initial accessibility of squares on an empty chessboard.
    :return: ndarray with ints representing the accessibility of a particular square
    """
    # Create 4 quarters
    left_upper_quarter = np.array([[2, 3, 4, 4], [3, 4, 6, 6], [4, 6, 8, 8], [4, 6, 8, 8]])
    right_upper_quarter = np.flip(left_upper_quarter, axis=1)
    right_lower_quarter = np.flip(left_upper_quarter)
    left_lower_quarter = np.flip(right_lower_quarter, axis=1)

    # Create upper and lower halves via concatenating quarters
    upper_half = np.hstack((left_upper_quarter, right_upper_quarter))
    lower_half = np.hstack((left_lower_quarter, right_lower_quarter))

    # Create board by stacking upper and lower halves
    board = np.vstack((upper_half, lower_half))
    # Return resulting accessibility board
    return board


def update_accessibility(curr_row, curr_col, access_matrix, list_of_moves):
    """
    Updates accessibility data based on current position and a list of valid moves
    :param curr_row: Int, current row
    :param curr_col: Int, current column
    :param access_matrix: 2D 8-by-8 array
    :param list_of_moves: List of tuples describing valid moves from current position (row_shift, col_shift)
    :return: ndarray with updated accessibility numbers
    """
    for tuple_of_shifts in list_of_moves:
        row_shift, col_shift = tuple_of_shifts
        access_matrix[curr_row + row_shift][curr_col + col_shift] -= 1
    return


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


def pick_optimal_move(curr_row, curr_col, list_of_moves, access_matrix):
    """
    Returns a tuple with move to the least accessible square. Random if many eligible moves.
    :param curr_row: Int, current row
    :param curr_col: Int, current column
    :param access_matrix: 2D 8-by-8 array
    :param list_of_moves: List of tuples describing valid moves from current position (row_shift, col_shift)
    :return: Tuple from the list_of_moves
    """
    # Create dictionary to hold moves as tuples and accessibility of corresponding target square
    accessible_per_move = dict()
    # Iterate over list of move tuples and add every move tuple as key and accessibility as value to the dict
    for tuple_of_shifts in list_of_moves:
        row_shift, col_shift = tuple_of_shifts
        accessible_per_move[tuple_of_shifts] = access_matrix[curr_row + row_shift][curr_col + col_shift]
    # Determine lowest accessibility  value
    lowest_accessibility = min(accessible_per_move.values())

    # Create list of all move tuples with this lowest accessibility value
    least_accessible_moves = [k for k in accessible_per_move.keys() if accessible_per_move[k] == lowest_accessibility]

    # Return move tuple with lowest accessibility (pick randomly if there are some)
    return least_accessible_moves[random.randrange(len(least_accessible_moves))]


def run_knights_tour(start_row=0, start_col=0):
    """
    Run Knight's Tour on an 8-by-8 board
    :return: Count of the last move made by Knight
    """
    # Initialize chessboard
    chessboard = draw_board()

    # Initialize accessibility matrix
    accessibility_matrix = draw_accessibility()

    # Initialize variables to hold position of the knight
    current_row = start_row
    current_col = start_col

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
        # Update accessibility matrix
        update_accessibility(current_row, current_col, accessibility_matrix, possible_moves)

        # If no possible move: stop tour and return count of moves made
        if len(possible_moves) == 0:
            knight_can_move = False
            continue
        # Else pick one move from possible moves and update position of Knight and count of moves
        else:
            v_shift, h_shift = pick_optimal_move(current_row, current_col, possible_moves, accessibility_matrix)
            current_row += v_shift
            current_col += h_shift
            count_moves += 1

    if count_moves == 64:
        print("Great job! Your Knight has toured across the whole chessboard!")
    else:
        print(f"Tour ended on move #: {count_moves}")
    print("The chessboard after Knight's Tour looks as follows:")
    print(chessboard)


run_knights_tour()
