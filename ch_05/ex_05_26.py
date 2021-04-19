"""
Use the methods developed in Exercise 5.25 to:
Write a script that deals two five-card poker hands (i.e., two lists of five-card tuples each),
evaluates each hand and determines which wins.
As each card is dealt, it should be removed from the list of tuples representing the deck.
"""
import random
import numpy as np


def initialize_deck():
    """
    Initializes a randomly shuffled deck of card
    :return: a list of randomly shuffled tuples, each tuple is (<Face>, <Suit>)
    """
    card_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    card_faces = ["Ace", "Deuce", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen",
                  "King"]

    deck = [(face, suit) for suit in card_suits for face in card_faces]
    random.shuffle(deck)

    return deck


def deal_hand(deck):
    """
    Deals a five-card poker hand as a list of five card tuples. Takes a list of tuples of args.
    Removes dealt cards (tuples) from the deck
    :param deck: A list containing tuples of cards
    :return: A list of 5 randomly selected tuples representing hand.
    """
    hand = list()
    for _ in range(5):
        random_index = random.randrange(len(deck))
        hand.append(deck[random_index])
        deck.pop(random_index)
    return hand


def is_one_pair_basic(hand):
    """
    Determines whether the hand passed as argument contains exactly one pair (two identical faces)
    Use basic features like lists and tuples and .count()
    :param hand: A list containing 5 card tuples
    :return: True if the hand contains exactly one pair
    """
    # Create a list of just faces
    faces = list(x[0] for x in hand)

    # Empty list to store faces with frequencies
    faces_w_freqs = list()

    # Iterate over faces and if not counted: count frequency of current face
    # Append as list [face, count]
    for face in faces:
        if face not in [y[0] for y in faces_w_freqs]:
            faces_w_freqs.append([face, faces.count(face)])

    # Check that only one frequency is 2 and no frequency is 3 present
    if 2 in [z[1] for z in faces_w_freqs] and [z[1] for z in faces_w_freqs].count(2) == 1 \
            and 3 not in [z[1] for z in faces_w_freqs]:
        pair_to_print = list(filter(lambda x: x[1] == 2, faces_w_freqs))
        print(f"You have one pair of {pair_to_print[0][0]}s")
        print(*hand)
        return True

    # If not exactly one pair: print corresponding message and display hand as proof
    print("You do not have exactly one pair. Your hand is:")
    print(*hand)
    return False


def is_one_pair_numpy(hand):
    """
    Determines whether the hand passed as argument contains exactly one pair (two identical faces)
    Use numpy functionality
    :param hand: A list containing 5 card tuples
    :return: True if the hand contains exactly one pair
    """
    # Generate 2 ndarrays holding faces and heir corresponding frequencies
    faces, frequencies = np.unique(list(x[0] for x in hand), return_counts=True)

    # Check that only one frequency is 2 and no frequency is 3 present
    if 2 in frequencies and list(frequencies).count(2) == 1 and 3 not in frequencies:
        pair_index = list(frequencies).index(2)
        print(f"You have one pair of {faces[pair_index]}s:")
        print(*hand)
        return True

    # If not exactly one pair: print corresponding message and display hand as proof
    return False


def is_two_pair(hand):
    """
    Determines whether the hand passed as argument contains exactly two pairs (2 x 2 identical faces)
    Use numpy functionality
    :param hand: A list containing 5 card tuples
    :return: True if the hand contains exactly two pairs
    """
    # Generate 2 ndarrays holding faces and heir corresponding frequencies
    faces, frequencies = np.unique(list(x[0] for x in hand), return_counts=True)
    faces, frequencies = list(faces), list(frequencies)

    # Check that only one frequency is 2 and no frequency is 3 present
    if 2 in frequencies and frequencies.count(2) == 2:
        faces.pop(frequencies.index(1))
        print(f"You have two pair: One pair of {faces[0]}s and one pair of {faces[1]}s:")
        print(*hand)
        return True

    # If not exactly two pair: print corresponding message and display hand as proof
    return False


def is_three_of_a_kind(hand):
    """
    Determines whether the hand passed as argument contains exactly three of a kind (3 identical faces)
    Use numpy functionality
    :param hand: A list containing 5 card tuples
    :return: True if the hand contains exactly three of a kind
    """
    # Generate 2 ndarrays holding faces and heir corresponding frequencies
    faces, frequencies = np.unique(list(x[0] for x in hand), return_counts=True)

    # Check that only one frequency is 2 and no frequency is 3 present
    if 3 in frequencies and 2 not in frequencies:
        print("You have three of a kind: ", end="")
        print(f"Three {faces[list(frequencies).index(3)]}s:")
        print(*hand)
        return True

    # If not exactly three of a kind: print corresponding message and display hand as proof
    return False


def is_four_of_a_kind(hand):
    """
    Determines whether the hand passed as argument contains exactly four of a kind(4 identical faces)
    Use numpy functionality
    :param hand: A list containing 5 card tuples
    :return: True if the hand contains exactly four of a kind
    """
    # Generate 2 ndarrays holding faces and heir corresponding frequencies
    faces, frequencies = np.unique(list(x[0] for x in hand), return_counts=True)

    # Check that only one frequency is 2 and no frequency is 3 present
    if 4 in frequencies:
        print("You have four of a kind: ", end="")
        print(f"Four {faces[list(frequencies).index(4)]}s:")
        print(*hand)
        return True

    # If not exactly four of a kind: print corresponding message and display hand as proof
    return False


def is_full_house(hand):
    """
    Determines whether the hand passed as argument contains exactly full-house(3 identical faces + 2 identical faces)
    Use numpy functionality
    :param hand: A list containing 5 card tuples
    :return: True if the hand contains exactly full-house
    """
    # Generate 2 ndarrays holding faces and heir corresponding frequencies
    faces, frequencies = np.unique(list(x[0] for x in hand), return_counts=True)

    # Check that only one frequency is 2 and no frequency is 3 present
    if 3 in frequencies and 2 in frequencies:
        print("You have a full-house: ", end="")
        print(f"Three {faces[list(frequencies).index(3)]}s and Two {faces[list(frequencies).index(2)]}s:")
        print(*hand)
        return True

    # If not exactly full-house: print corresponding message and display hand as proof
    return False


def is_ascending_by_one(int_arr):
    """
    Determines whether the values in the list increase consequently by 1
    :param int_arr: List of integer values
    :return: True if values increase consequently by 1, else False
    """
    for i in range(len(int_arr) - 1):
        if int_arr[i + 1] - int_arr[i] != 1:
            return False
    return True


def is_straight(hand):
    """
    Determines whether the hand passed as argument contains exactly straight (5 consequent suits)
    Use numpy functionality
    :param hand: A list containing 5 card tuples
    :return: True if the hand contains exactly straight but not straight flush
    """
    faces_to_nums_ace_one = {"Ace": 1, "Deuce": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8,
                             "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 12, "King": 13}
    faces_to_nums_ace_fourteen = {"Deuce": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8,
                                  "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

    suits, suits_freqs = np.unique(list(x[1] for x in hand), return_counts=True)
    faces, faces_freqs = np.unique(list(x[0] for x in hand), return_counts=True)
    # Check that all faces are different == there are 5 faces
    if len(faces) != 5:
        return False

    # If there are five different faces: check that they are not of same suit
    if 5 in suits_freqs:
        return False

    if "Ace" not in faces:
        numerical_faces_ascending = sorted(list(map(lambda x: faces_to_nums_ace_one[x], faces)))
        if not is_ascending_by_one(numerical_faces_ascending):
            return False

    else:  # if Ace in faces
        num_faces_ascend_ace_one = sorted(list(map(lambda x: faces_to_nums_ace_one[x], faces)))
        num_faces_ascend_ace_fourteen = sorted(list(map(lambda x: faces_to_nums_ace_fourteen[x], faces)))

        if not (is_ascending_by_one(num_faces_ascend_ace_one) or is_ascending_by_one(num_faces_ascend_ace_fourteen)):
            return False

    print("You have a straight:")
    print(*hand)
    return True


def is_flush(hand):
    """
    Determines whether the hand passed as argument contains exactly flush (5 cards of same suit)
    Use numpy functionality
    :param hand: A list containing 5 card tuples
    :return: True if the hand contains exactly flush but not straight flush
    """
    # Generate 2 ndarrays holding faces and heir corresponding frequencies
    suits, frequencies = np.unique(list(x[1] for x in hand), return_counts=True)

    # Check that only one frequency is 2 and no frequency is 3 present
    if 5 in frequencies and not is_straight(hand):
        print("You have a flush: ", end="")
        print(f"Five cards of {suits[0]} suit: ")
        print(*hand)
        return True

    # If not exactly flush: print corresponding message and display hand as proof
    return False


def is_straight_flush(hand):
    """
    Determines whether the hand passed as argument contains straight flush (5 cards of same suit of consecutive faces)
    Use numpy functionality
    :param hand: A list containing 5 card tuples
    :return: True if the hand contains straight flush
    """
    faces_to_nums_ace_one = {"Ace": 1, "Deuce": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8,
                             "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 12, "King": 13}

    suits, suits_freqs = np.unique(list(x[1] for x in hand), return_counts=True)
    faces, faces_freqs = np.unique(list(x[0] for x in hand), return_counts=True)

    if 5 not in suits_freqs:
        return False

    num_faces_ascend = sorted(list(map(lambda x: faces_to_nums_ace_one[x], faces)))
    if not is_ascending_by_one(num_faces_ascend):
        return False

    print("You have a straight flush:")
    print(*hand)
    return True


def is_royal_flush(hand):
    """
    Determines whether the hand passed as argument contains royal flush (5 cards of same suit A to T)
    Use numpy functionality
    :param hand: A list containing 5 card tuples
    :return: True if the hand contains royal flush
    """
    suits, suits_freqs = np.unique(list(x[1] for x in hand), return_counts=True)
    faces, faces_freqs = np.unique(list(x[0] for x in hand), return_counts=True)

    if 5 not in suits_freqs:
        return False

    if any([True for x in faces if x not in ("Ace", "King", "Queen", "Jack", "Ten")]):
        return False

    print("You have a royal flush:")
    print(*hand)
    return False


strength_combination_map = {1: is_one_pair_numpy, 2: is_two_pair, 3: is_three_of_a_kind, 4: is_straight, 5: is_flush,
                            6: is_full_house, 7: is_four_of_a_kind, 8: is_straight_flush, 9: is_royal_flush}


def determine_hand_strength(hand: list, values_combs: dict = strength_combination_map):
    """
    Determines hand strength (value) from 0 (no combination) to 9 (royal flush)
    :param hand: A list of 5 tuples, each tuple represents "Face" and "Suit"
    :param values_combs: Dictionary mapping integer value to corresponding function names determining combinations.
    :return: Integer value which corresponds to combination or 0 if no combination could be found.
    """
    hand_value = 0
    # Iterate over function combinations. If any returns True: return corresponding hand strength int
    for strength, function in values_combs.items():
        if function(hand):
            print(f"This hand got you {strength} points.")
            hand_value = strength
            return hand_value
    print("You have no valid combination:")
    print(*hand)
    print("This hand got you 0 points.")
    return hand_value


def compare_two_hands(hand1: list, hand2: list):
    """
    Compares the strength of two hands and prints out the winner
    :param hand1: A list of 5 tuples, each tuple represents "Face" and "Suit"
    :param hand2: A list of 5 tuples, each tuple represents "Face" and "Suit"
    :return: Prints who wins: hand1 or hand2
    """
    print()
    print("Determining the strength of Player 1's hand:...")
    score_player_1 = determine_hand_strength(hand1)

    print("-------------------------")

    print("Determining the strength of Player 2's hand:...")
    score_player_2 = determine_hand_strength(hand2)

    print("-------------------------")
    if score_player_1 > score_player_2:
        print(f"Player 1 wins by having {score_player_1} point(s) against {score_player_2} point(s).")
    elif score_player_2 > score_player_1:
        print(f"Player 2 wins by having {score_player_2} point(s) against {score_player_1} point(s).")
    else:
        print(f"It's a draw, since both players have {score_player_2} point(s).")
    return


strength_combination_map = {1: is_one_pair_numpy, 2: is_two_pair, 3: is_three_of_a_kind, 4: is_straight, 5: is_flush,
                            6: is_full_house, 7: is_four_of_a_kind, 8: is_straight_flush, 9: is_royal_flush}

deck_of_cards = initialize_deck()

dealt_hand_player_1 = deal_hand(deck_of_cards)
dealt_hand_player_2 = deal_hand(deck_of_cards)

compare_two_hands(dealt_hand_player_1, dealt_hand_player_2)
