# Exercise 07_12 from Deitel: Intro to Python for CS

"""
Develop a script that plays three-dimensional Tic-Tac-Toe on a 4-by-4-by-4 board.
"""

import numpy as np
import random


def get_valid_move_human(board, filler="-"):
    """
    Repeatedly asks for input until valid (unfilled) square coordinates are entered.
    :param board: NumPy array 3x3 containing "X"s, "O"s and filler
    :param filler: Str, what is used to fill the board ("-" is default)
    :return: A tuple containing row and col coordinates as ints
    """
    # Ask user to enter coordinates for his move
    plane, row, col = map(int, input("Enter your move: ").split())

    # Initialize flag to control correct / incorrect input
    is_valid_move = False

    # Repeat until is_valid_move becomes True = valid move entered
    while not is_valid_move:
        # Check if coordinates are out of range
        if max(plane, row, col) > 3 or min(plane, row, col) < 0:
            print("Coordinates out of range. Try again.", end=" ")
            # Ask user to enter coordinates for his move
            plane, row, col = map(int, input("Enter your move: ").split())
            continue
        elif board[plane][row][col] != filler:
            print("This square is not empty. Try again.", end=" ")
            # Ask user to enter coordinates for his move
            plane, row, col = map(int, input("Enter your move: ").split())
            continue
        else:
            is_valid_move = True

    return plane, row, col


def get_valid_move_robot(board, filler="-"):
    """
    Repeatedly get random coordinates from PC until valid (unfilled) square coordinates are entered.
    :param board: NumPy array 3x3 containing "X"s, "O"s and filler
    :param filler: Str, what is used to fill the board ("-" is default)
    :return: A tuple containing row and col coordinates as ints
    """
    # Ask user to enter coordinates for his move
    plane, row, col = (random.randrange(board.shape[0]) for _ in range(3))

    # Initialize flag to control correct / incorrect input
    is_valid_move = False

    # Repeat until is_valid_move becomes True = valid move entered
    while not is_valid_move:
        # Check if coordinates are out of range
        if board[plane][row][col] != filler:
            # Ask robot to generate new random coordinates for his move
            plane, row, col = (random.randrange(board.shape[0]) for _ in range(3))
            continue
        else:
            is_valid_move = True

    return plane, row, col


def draw_tic_tac_board(num_planes=4, num_rows=4, num_cols=4, filler="-"):
    """
    Returns a NumPy array of specified shape (4x4x4 by default) filled with filler ("-" default)
    :param num_planes: Int, number of (levels) planes in the board, 4 by default
    :param num_rows: Int, number of rows in the board, 4 by default
    :param num_cols: Int, number of cols in the board, 4 by default
    :param filler: Str, with what to fill every cell, "-' by default
    :return: NumPy array
    """
    # Create initial board of given shape and populate with "1" as str
    board = np.arange(num_planes * num_rows * num_cols).astype(int).astype(str).reshape(num_planes, num_rows, num_cols)

    # Replace the initial "1"s with specified filler
    # Iterate over indices of planes:
    for k in range(num_planes):
        # Iterate over indices of rows
        for i in range(num_rows):
            # Iterate over indices of cols
            for j in range(num_cols):
                board[k][i][j] = filler

    return board


def check_plane_for_winner(board, symbol: str):
    """
    Checks whether on individual 2D plane there is n symbols in a horizontal or vertical row or in diagonal
    :param board: 2D NumPy array of given size
    :param symbol: "X" or "O" for corresponding player
    :return: True (if game won) or False (if not)
    """
    # Check horizontally:
    for row in board:
        if all(row == symbol):
            return True

    # Check vertically:
    for col in range(board.shape[1]):
        if all(board[:, col] == symbol):
            return True

    # Check diagonally
    diagonal_1 = np.array([True])
    diagonal_2 = np.array([True])

    # Check diagonal_1
    i, j = 0, 0
    for level in range(board.shape[0]):
        diagonal_1 = np.append(diagonal_1, board[i][j] == symbol)
        i += 1
        j += 1
    if all(diagonal_1):
        return True

    # Check diagonal_2
    i, j = board.shape[0] - 1,  0
    for level in range(board.shape[0]):
        diagonal_2 = np.append(diagonal_2, board[i][j] == symbol)
        i -= 1
        j += 1
    if all(diagonal_2):
        return True

    return False


def check_board_for_winner(board, symbol: str):
    """
    Checks whether on the given 3D board there is n symbols in a horizontal or vertical row or in diagonal
    :param board: 3D NumPy array
    :param symbol: "X" or "O" for corresponding player
    :return: True (if game won) or False (if not)
    """
    # Determine board size
    board_size = board.shape[0]

    # Check individual planes in every dimension
    for i in range(board_size):
        # By Planes
        if check_plane_for_winner(board[i, :, :], symbol):
            return True
        # By Rows
        if check_plane_for_winner(board[:, i, :], symbol):
            return True
        # By Columns
        if check_plane_for_winner(board[:, :, i], symbol):
            return True

    # Check for two diagonals:
    diagonal_1 = np.array([True])
    diagonal_2 = np.array([True])

    # Check diagonal_1
    k, i, j = 0, 0, 0
    for level in range(board_size):
        diagonal_1 = np.append(diagonal_1, board[k][i][j] == symbol)
        k += 1
        i += 1
        j += 1
    if all(diagonal_1):
        return True

    # Check diagonal_2
    k, i, j = board_size - 1, 0, 0
    for level in range(board.shape[0]):
        diagonal_2 = np.append(diagonal_2, board[k][i][j] == symbol)
        k -= 1
        i += 1
        j += 1
    if all(diagonal_2):
        return True


def check_for_tie(board, filler="-"):
    """
    Checks whether the game ended with a tie (draw)
    :param board: NumPy array as a board
    :param filler: Str, filler for the board squares, "-" is default value
    :return: True if no 'empty' squares left in the board
    """
    return filler not in board


def play_human_vs_robot():
    """
    Plays a 3D game of 4x4x4 tic-tac-toe between Human and Robot players. Human begins.
    :return: Winner or Tie as a string
    """
    # Initialize board and populate with ones
    tic_tac_toe_board = draw_tic_tac_board()
    print(tic_tac_toe_board)

    # Initialize counter of moves: even moves = Player1, odd moves = Player2
    counter_moves = 0

    # Initialize flag to keep track if the game has ended or not and who won
    winner_is_human = False
    winner_is_robot = False
    ended_with_tie = False
    game_ended = False

    # Repeat while game has not ended:
    while not game_ended:

        # Getting input and checking result for Human
        if counter_moves % 2 == 0:
            print("Human plays. ", end="")
            # Get input and update board
            plane_ind, row_ind, col_ind = get_valid_move_human(tic_tac_toe_board)
            tic_tac_toe_board[plane_ind][row_ind][col_ind] = "X"
            # Check if Human has won with this move
            winner_is_human = game_ended = check_board_for_winner(tic_tac_toe_board, "X")

        # Getting input and checking result for Robot
        elif counter_moves % 2 == 1:
            print("Robot plays. Board after Robot;s move:")
            plane_ind, row_ind, col_ind = get_valid_move_robot(tic_tac_toe_board)
            tic_tac_toe_board[plane_ind][row_ind][col_ind] = "O"
            winner_is_robot = game_ended = check_board_for_winner(tic_tac_toe_board, "O")

        # Check for draw (tie)
        if not (winner_is_robot or winner_is_human):
            ended_with_tie = game_ended = check_for_tie(tic_tac_toe_board)
        counter_moves += 1
        print(tic_tac_toe_board)

    if winner_is_human:
        print("Human has won!")
    elif winner_is_robot:
        print("Robot has won!")
    elif ended_with_tie:
        print("Game ended with tie!")


def play_robot_vs_human():
    """
    Plays a game of tic-tac-toe between Human and Robot players. Robot begins.
    :return: Winner or Tie as a string
    """
    # Initialize board and populate with ones
    tic_tac_toe_board = draw_tic_tac_board()
    print(tic_tac_toe_board)

    # Initialize counter of moves: even moves = Player1, odd moves = Player2
    counter_moves = 0

    # Initialize flag to keep track if the game has ended or not and who won
    winner_is_human = False
    winner_is_robot = False
    ended_with_tie = False
    game_ended = False

    # Repeat while game has not ended:
    while not game_ended:

        # Getting input and checking result for Human
        if counter_moves % 2 == 1:
            print("Human plays. ", end="")
            # Get input and update board
            plane_ind, row_ind, col_ind = get_valid_move_human(tic_tac_toe_board)
            tic_tac_toe_board[plane_ind][row_ind][col_ind] = "O"
            # Check if Human has won with this move
            winner_is_human = game_ended = check_board_for_winner(tic_tac_toe_board, "O")

        # Getting input and checking result for Robot
        elif counter_moves % 2 == 0:
            print("Robot plays. Board after Robot's move:")
            plane_ind, row_ind, col_ind = get_valid_move_robot(tic_tac_toe_board)
            tic_tac_toe_board[plane_ind][row_ind][col_ind] = "X"
            winner_is_robot = game_ended = check_board_for_winner(tic_tac_toe_board, "X")

        # Check for draw (tie)
        if not (winner_is_robot or winner_is_human):
            ended_with_tie = game_ended = check_for_tie(tic_tac_toe_board)
        counter_moves += 1
        print(tic_tac_toe_board)

    if winner_is_human:
        print("Human has won!")
    elif winner_is_robot:
        print("Robot has won!")
    elif ended_with_tie:
        print("Game ended with tie!")


human_first = bool(int(input("Who should start? 0 for Robot, 1 for Human: ")))

if human_first:
    play_human_vs_robot()
else:
    play_robot_vs_human()
