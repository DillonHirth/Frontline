from decks import Deck as Deck


class Player:
    """Player class that should own a 2 decks, a hand of cards, and half the game-board

    Methods:
        draw_hand
    """

    def __init__(self, player_name):
        suit_list = ['Spade', 'Diamond', 'Club', 'Heart']
        numerical_value_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        face_value_list = ['Jack', 'Queen', 'King', 'Ace', 'Joker']

        self.player_name = player_name
        self.main_deck = Deck(numerical_value_list, suit_list)
        self.support_deck = Deck(face_value_list, suit_list)

    def __repr__(self):
        return f"{self.value} of {self.suit}s, Skill: {self.ability}"
