"""
Modify Exercise 5.24 to deal a five-card poker hand as a list of five card tuples.
Then create functions (i.e., is_pair, is_two_pair, is_three_of_a_kind, …)
that determine whether the hand they receive as an argument contains groups of cards, such as one pair etc.
Assign numerical value to hand based on cards they receive
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
    Determines whether the hand passed asa argument contains exactly one pair (two identical faces)
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
    if 2 in [z[1] for z in faces_w_freqs] and [z[1] for z in faces_w_freqs].count(2) == 1\
            and 3 not in [z[1] for z in faces_w_freqs]:
        pair_to_print = list(filter(lambda x: x[1] == 2, faces_w_freqs))
        print(f"You have one pair of {pair_to_print[0][0]}s")
        print(hand)
        return True

    # If not exactly one pair: print corresponding message and display hand as proof
    print("You do not have exactly one pair. Your hand is:")
    print(hand)
    return False


def is_one_pair_numpy(hand):
    """
    Determines whether the hand passed asa argument contains exactly one pair (two identical faces)
    Use numpy functionality
    :param hand: A list containing 5 card tuples
    :return: True if the hand contains exactly one pair
    """
    # Generate 2 ndarrays holding faces and heir corresponding frequencies
    faces, frequencies = np.unique(list(x[0] for x in hand), return_counts=True)

    # Check that only one frequency is 2 and no frequency is 3 present
    if 2 in frequencies and list(frequencies).count(2) == 1 and 3 not in frequencies:
        pair_index = list(frequencies).index(2)
        print(f"You have one pair of {faces[pair_index]}s")
        print(hand)
        return True

    # If not exactly one pair: print corresponding message and display hand as proof
    print("You do not have exactly one pair. Your hand is:")
    print(hand)
    return False


deck_of_cards = initialize_deck()
dealt_hand = deal_hand(deck_of_cards)

is_one_pair_basic(dealt_hand)
print("------------------------------------------")
is_one_pair_numpy(dealt_hand)

# print(dealt_hand)
# print(len(deck_of_cards))
