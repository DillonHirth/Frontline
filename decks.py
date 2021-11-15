"""
random:
    https://docs.python.org/3/library/random.html
"""
import random


class Card:
    """card class, very simple, probably an over complication,
    but I'm waiting to see how pygame works. before i turn it into a dictionary or namedtuple"""

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.ability = " "

    def __repr__(self):
        return f"{self.value} of {self.suit}s, Skill: {self.ability}"


class Deck:
    """main army deck, generates a 36 count deck of numerical cards

    Methods:
        generate_main_deck
        card_count
        draw
        shuffle
    """
    def __init__(self, suit_list, value_list):
        self.suit_list = suit_list
        self.value_list = value_list
        self.generated_deck = self.generate_deck()

    def __repr__(self):
        return f"generated_deck: {self.generated_deck}"

    def generate_deck(self):
        """generates a list of 36 CARD objects, with a numerical value for each suit"""

        deck_list = []
        for suit in self.suit_list:
            for value in self.value_list:
                deck_list.append(Card(value, suit))
        return deck_list

    def card_count(self):
        """returns the length of the generated deck"""

        return len(self.generated_deck)

    def draw(self):
        """pops the first card off of the deck and returns it"""

        return self.generated_deck.pop(0)

    def shuffle(self):
        """uses random.shuffle() to shuffle the list and returns a
        reference to the MainDeck object"""

        random.shuffle(self.generated_deck)
        return self
