# Exercise 10_21 from Deitel: Intro to Python and CS

"""
Using the DeckOfCards class from this chapter, create a simple Blackjack game.

The rules of the game are as follows:
• Two cards each are dealt to the dealer and the player. The player’s cards are dealt face up.
Only one of the dealer’s cards is dealt face up.
• Each card has a value. A card numbered 2 through 10 is worth its face value. Jacks, queens and kings each count as 10.
Aces can count as 1 or 11—whichever value is more beneficial to the player.
• If the sum of the player’s first two cards is 21
(that is, the player was dealt a card valued at 10 and an ace, which counts as 11 in this situation),
the player has “blackjack” and immediately wins the game —
if the dealer does not also have blackjack, which would result in a “push” (or tie).
• Otherwise, the player can begin taking additional cards one at a time.
These cards  are dealt face up, and the player decides when to stop taking cards.
If the player “busts” (that is, the sum of the player’s cards exceeds 21), the game is over and the player loses.
When the player is satisfied with the current set of cards, the player “stands” (that is, stops taking cards),
and the dealer’s hidden card is revealed.
• If the dealer’s total is 16 or less, the dealer must take another card; otherwise, the dealer must stand.
The dealer must continue taking cards until the sum of the cards is greater than or equal to 17.
If the dealer exceeds 21, the player wins. Otherwise, the hand with the higher point total wins.
If the dealer and the player have the same point total, the game is a “push,” and no one wins.

An ace’s value for a dealer depends on the dealer’s other card(s) and the casino’s house rules.
A dealer typically must hit for totals of 16 or less and must stand for 17 or more.
For a “soft 17”—a total of 17 with one ace counted as 11—some casinos require the dealer to hit
and some require the dealer to stand (we require the dealer to stand).
Such a hand is known as a “soft 17” because taking another card cannot bust the hand.

Enable a player to interact with the game using the keyboard—
'H' means hit (take another card and 'S' means stand (do not take another card).
Display the dealer’s and player’s hands as card images using Matplotlib, as we did in this chapter.
"""

import random
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# plt.ion()


class Card:
    FACES = ['Ace', '2', '3', '4', '5', '6',
             '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, face, suit):
        """Initialize a Card with a face and suit."""
        self._face = face
        self._suit = suit

    @property
    def face(self):
        """Return the Card's self._face value."""
        return self._face

    @property
    def suit(self):
        """Return the Card's self._suit value."""
        return self._suit

    @property
    def image_name(self):
        """Return the Card's image file name."""
        return str(self).replace(' ', '_') + '.png'

    def __repr__(self):
        """Return string representation for repr()."""
        return f"Card(face='{self.face}', suit='{self.suit}')"

    def __str__(self):
        """Return string representation for str()."""
        return f'{self.face} of {self.suit}'

    def __format__(self, format):
        """Return formatted string representation."""
        return f'{str(self):{format}}'


class DeckOfCards:
    NUMBER_OF_CARDS = 52  # constant number of Cards

    def __init__(self):
        """Initialize the deck."""
        self._current_card = 0
        self._deck = []

        for count in range(DeckOfCards.NUMBER_OF_CARDS):
            self._deck.append(Card(Card.FACES[count % 13],
                                   Card.SUITS[count // 13]))

    def shuffle(self):
        """Shuffle deck."""
        self._current_card = 0
        random.shuffle(self._deck)

    def deal_card(self):
        """Return one Card."""
        try:
            card = self._deck[self._current_card]
            self._current_card += 1
            return card
        except:
            return None

    def __str__(self):
        """Return a string representation of the current _deck."""
        s = ''

        for index, card in enumerate(self._deck):
            s += f'{self._deck[index]:<19}'
            if (index + 1) % 4 == 0:
                s += '\n'

        return s


class Hand:
    FACES_SCORES = {'Ace': 11, 'King': 10, 'Queen': 10, 'Jack': 10, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5,
                    '4': 4, '3': 3, '2': 2}
    """Class to represent player's or dealer's hand as a list of cards."""
    def __init__(self, card1, card2, first_invisible=False):
        self.list_of_cards = [card1, card2]
        self.first_invisible = first_invisible
        self.list_of_scores = self.calculate_score()

    def calculate_score(self):
        count_aces = 0
        scores = [0, 0]
        for card in self.list_of_cards:
            if 'Ace' in card.face:
                count_aces += 1
            else:
                scores[0] += Hand.FACES_SCORES[card.face]
                scores[1] += Hand.FACES_SCORES[card.face]

        if count_aces != 0:
            scores[0] += 1 * count_aces
            scores[1] += 10 + 1 * count_aces
        self.list_of_scores = scores
        return scores

    def add_card(self, card):
        self.list_of_cards.append(card)

    def displayable_score(self):
        val1 = self.list_of_scores[0]
        val2 = self.list_of_scores[1]
        if val1 == val2:
            return str(val1)
        elif val1 > 21 and val2 > 21:
            return str(min(val1, val2))
        elif val1 > 21 or val2 > 21:
            return str(min(val1, val2))
        else:
            return f'{val1} or {val2}'

    def exceeds_twenty_one(self):
        if 21 < self.list_of_scores[0] and 21 < self.list_of_scores[1]:
            return True
        return False

    def seventeen_or_more(self):
        if 17 <= self.list_of_scores[0] <= 21 or 17 <= self.list_of_scores[1] <= 21:
            return True
        return False

    def best_possible_score(self):
        val1 = self.list_of_scores[0]
        val2 = self.list_of_scores[1]
        if val1 == val2:
            return val1
        elif val1 <= 21 and val2 <= 21:
            return max(val1, val2)
        else:
            return min(val1, val2)

    def can_continue(self):
        val1 = self.list_of_scores[0]
        val2 = self.list_of_scores[1]
        if val1 > 21 and val2 > 21:
            return False
        return True


def display_hands(player_hand, dealer_hand):
    # Creating figure with 2 rows and 5 slots for cards
    figure, axes_list = plt.subplots(nrows=2, ncols=6)
    # Setting title for Player's Score
    axes_list[0, 0].set_title(f"Player's Cards and Score: {player_hand.displayable_score()}")
    # Setting title for Dealer's Score
    if dealer_hand.first_invisible:
        axes_list[1, 0].set_title(f"Dealer's Cards and Score: Unknown")
    else:
        axes_list[1, 0].set_title(f"Dealer's Cards and Score: {dealer_hand.displayable_score()}")

    # Formatting nicely
    for axis in axes_list.ravel():
        axis.get_xaxis().set_visible(False)
        axis.get_yaxis().set_visible(False)

    # Create path object to access the images
    path = Path('.').joinpath('card_images')

    # Displaying cards of the player
    for i in range(len(player_hand.list_of_cards)):
        image_name = player_hand.list_of_cards[i].image_name
        img = mpimg.imread(str(path.joinpath(image_name).resolve()))
        axes_list[0, i].imshow(img)

    # Displaying cards of the dealer
    if dealer_hand.first_invisible:
        img = mpimg.imread(str(path.joinpath("back_of_card.png").resolve()))
        axes_list[1, 0].imshow(img)

        for i in range(1, len(dealer_hand.list_of_cards)):
            image_name = dealer_hand.list_of_cards[i].image_name
            img = mpimg.imread(str(path.joinpath(image_name).resolve()))
            axes_list[1, i].imshow(img)
    else:
        for i in range(len(dealer_hand.list_of_cards)):
            image_name = dealer_hand.list_of_cards[i].image_name
            img = mpimg.imread(str(path.joinpath(image_name).resolve()))
            axes_list[1, i].imshow(img)

    # Showing the resulting figure
    plt.show()


def blackjack_at_start(player_hand, dealer_hand):
    player_scores = player_hand.calculate_score()
    if 21 in player_scores:
        dealer_scores = dealer_hand.calculate_score()
        dealer_hand.first_invisible = False
        if 21 in dealer_scores:
            print("It's a tie!")
            display_hands(player_hand, dealer_hand)
            return True
        else:
            print("Player won!")
            display_hands(player_hand, dealer_hand)
            return True
    return False


# Initial setup
# Generate a deck of cards
deck = DeckOfCards()

# Shuffle the deck 5 times
for i in range(5):
    deck.shuffle()

# Deal 2 cards to player and dealer
# pl_hand = Hand(deck.deal_card(), deck.deal_card())
pl_hand = Hand(deck.deal_card(), deck.deal_card())
dl_hand = Hand(deck.deal_card(), deck.deal_card(), first_invisible=True)

# Display initial setup
display_hands(pl_hand, dl_hand)

# Start the game
game_over = False
player_acts = True
dealer_acts = True

# Check for blackjack at start
if blackjack_at_start(pl_hand, dl_hand):
    game_over = True
    dealer_acts = False
    player_acts = False

# Player acts
while player_acts:
    if pl_hand.exceeds_twenty_one():
        game_over = True
        player_acts = False
        dealer_acts = False
        print("Player has lost!")
        dl_hand.first_invisible = False
        display_hands(pl_hand, dl_hand)
        continue
    else:
        player_decision = input("Please press 's' to stand or 'h' to hit: ")
        if player_decision == 's':
            player_acts = False
            print("Now the dealer should act!")
            dl_hand.first_invisible = False
            display_hands(pl_hand, dl_hand)
            continue
        else:
            pl_hand.add_card(deck.deal_card())
            pl_hand.calculate_score()
            display_hands(pl_hand, dl_hand)

# Dealer acts
while dealer_acts:
    dl_hand.first_invisible = False
    if dl_hand.exceeds_twenty_one():
        game_over = True
        dealer_acts = False
        print("Player has won!")
        dl_hand.first_invisible = False
        display_hands(pl_hand, dl_hand)
        continue
    elif dl_hand.seventeen_or_more():
        dealer_acts = False
        continue
    else:
        dl_hand.add_card(deck.deal_card())
        dl_hand.calculate_score()
        display_hands(pl_hand, dl_hand)

# Determine winner if nobody exceeded 21
if not game_over:
    player_score = pl_hand.best_possible_score()
    dealer_score = dl_hand.best_possible_score()

    if player_score == dealer_score:
        print("It's a tie!")
    elif player_score > dealer_score:
        print("Player has won!")
    else:
        print("Dealer has won!")
dl_hand.first_invisible = False
display_hands(pl_hand, dl_hand)
