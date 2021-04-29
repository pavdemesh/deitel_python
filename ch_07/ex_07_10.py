# Exercise 07_10 from Deitel: Intro to Python for CS

"""
Write a script to play 2D Tic-Tac-Toe between two human players who alternate entering their moves.
Use a 3-by-3 two-dimensional array.
Each player indicates their moves by:
entering a pair of numbers representing the row and column indices of the square in which they want to place their mark,
either an 'X' or an 'O'.
When the first player moves, place an 'X' in the specified square.
When the second player moves, place an 'O' in the specified square.
ach move must be to an empty square.
After each move, determine whether the game has been won and whether it’s a draw.
"""

import numpy as np


def get_valid_move(board, filler="-"):
    """
    Repeatedly asks for input until valid (unfilled) square coordinates are entered.
    :param board: NumPy array 3x3 containing "X"s, "O"s and filler
    :param filler: Str, what is used to fill the board ("-" is default)
    :return: A tuple containing row and col coordinates as ints
    """
    # Ask user to enter coordinates for his move
    row, col = map(int, input("Enter your move: ").split())

    # Initialize flag to control correct / incorrect input
    is_valid_move = False

    # Repeat until is_valid_move becomes True = valid move entered
    while not is_valid_move:
        # Check if coordinates are out of range
        if (row > 2 or row < 0) or (col > 2 or col < 0):
            print("Coordinates out of range. Try again.", end=" ")
            # Ask user to enter coordinates for his move
            row, col = map(int, input("Enter your move: ").split())
            continue
        elif board[row][col] != "-":
            print("This square is not empty. Try again.", end=" ")
            # Ask user to enter coordinates for his move
            row, col = map(int, input("Enter your move: ").split())
            continue
        else:
            is_valid_move = True

    return row, col


def draw_tic_tac_board(num_rows=3, num_cols=3, filler="-"):
    """
    Returns a NumPy array of specified shape (3x3 default) filled with filler ("-" default)
    :param num_rows: Int, number of rows in the board, 3 by default
    :param num_cols: Int, number of cols in the board, 3 by default
    :param filler: Str, with what to fill every cell, "-' by default
    :return: NumPy array
    """
    # Create initial board of given shape and populate with "1" as str
    board = np.ones(num_rows * num_cols).astype(int).astype(str).reshape(num_rows, num_cols)

    # Replace the initial "1"s with specified filler
    # Iterate over indices of rows
    for i in range(num_rows):
        # Iterate over indices of cols
        for j in range(num_cols):
            board[i][j] = filler

    return board


def check_for_winner(board, symbol: str):
    """
    Checks where on given board there is three symbols in a row or in diagonal
    :param board: NumPy array of given size
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


def check_for_tie(board, filler="-"):
    """
    Checks whether the game ended with a tie (draw)
    :param board: NumPy array as a board
    :param filler: Str, filler for the board squares, "-" is default value
    :return: True if no 'empty' squares left in the board
    """
    return filler not in board


def play_tic_tac_toe():
    """
    Plays a game of tic-tac-toe between two human players
    :return: Winner or Tie as a string
    """
    # Initialize board and populate with ones
    tic_tac_toe_board = draw_tic_tac_board()
    print(tic_tac_toe_board)

    # Initialize counter of moves: even moves = Player1, odd moves = Player2
    counter_moves = 0

    # Initialize flag to keep track if the game has ended or not and who won
    player_one_won = False
    player_two_won = False
    ended_with_tie = False
    game_ended = False

    # Repeat while game has not ended:
    while not game_ended:

        # Getting input and checking result for Player 1
        if counter_moves % 2 == 0:
            print("Player 1. ", end="")
            # Get input and update board
            row_ind, col_ind = get_valid_move(tic_tac_toe_board)
            tic_tac_toe_board[row_ind][col_ind] = "X"
            # Check if he has won with this move
            player_one_won = game_ended = check_for_winner(tic_tac_toe_board, "X")

        # Getting input and checking result for Player 2
        elif counter_moves % 2 == 1:
            print("Player 2. ", end="")
            row_ind, col_ind = get_valid_move(tic_tac_toe_board)
            tic_tac_toe_board[row_ind][col_ind] = "O"
            player_two_won = game_ended = check_for_winner(tic_tac_toe_board, "O")

        # Check for draw (tie)
        if not (player_one_won or player_two_won):
            ended_with_tie = game_ended = check_for_tie(tic_tac_toe_board)
        counter_moves += 1
        print(tic_tac_toe_board)

    if player_one_won:
        print("Player 1 has won!")
    elif player_two_won:
        print("Player 2 has won!")
    else:
        print("Game ended with tie!")


play_tic_tac_toe()
