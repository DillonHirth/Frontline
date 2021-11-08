class Card:
    """

    """
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return "{} of {}s".format(self.value, self.suit)


class MainDeck:
    """
    """
    def __init__(self, deck_count=1):
        self.deck_count = deck_count
        self.generated_deck = self.generate_main_deck()

    def __repr__(self):
        return "generated_deck: {}".format(self.generated_deck)

    def generate_main_deck(self):
        suit_list = ['Spade', 'Diamond', 'Club', 'Heart']
        value_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        deck_list = []
        for suit in suit_list:
            for value in value_list:
                deck_list.append(Card(value, suit))
        return deck_list
    # count()
    # draw()
    # shuffle()


class SupportDeck(Card):
    """
    """
    suit = ['Spade', 'Diamond', 'Club', 'Heart']
    value_list = ['Jack', 'Queen', 'King', 'Ace', 'Joker']
    ## methods
    # count()
    # draw()
    # shuffle()
