from decks import Deck as Deck
from hand import Hand as Hand


class Player:
    """Player class that should own a 2 decks, a hand of cards, and half the game-board

    Methods:
        draw_hand
    """

    def __init__(self, player_name, deck_point_count, suit_list):
        self.deck_point_count = deck_point_count
        self.suit_list = suit_list
        self.numerical_value_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.face_value_list = ['Jack', 'Queen', 'King', 'Ace', 'Joker']

        self.player_name = player_name
        self.main_deck = Deck(self.numerical_value_list, self.suit_list).shuffle()
        self.support_deck = Deck(self.face_value_list, self.suit_list).shuffle()
        self.player_starting_hand = Hand(self.main_deck, self.deck_point_count)

    # def __repr__(self):
    #     return f"{self.value} of {self.suit}s, Skill: {self.ability}"
