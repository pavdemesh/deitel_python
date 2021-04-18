"""
Create an initialize_deck function to initialize the deck of card tuples with 'Ace' through 'King' of each suit, as in
deck = [('Ace', 'Hearts'), …, ('King', 'Hearts'),
('Ace', 'Diamonds'), …, ('King', 'Diamonds'),
('Ace', 'Clubs'), …, ('King', 'Clubs'),
('Ace', 'Spades'), …, ('King', 'Spades')]
"""
import random


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


deck_of_cards = initialize_deck()

# Output the shuffled cards in the  four-column format:
for i in range(13):
    for j in range(4):
        card_index = i * 4 + j
        card_name = f"{deck_of_cards[card_index][0]} of {deck_of_cards[card_index][1]}"
        print(card_name.ljust(20), end="")
    print()
