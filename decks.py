class Card:
    """
    basic card object, has value and suit
    """

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return "{} of {}s".format(self.value, self.suit)


class MainDeck:
    """main army deck, generates a 36 count deck of number cards

    Methods:
    card_count
    draw
    shuffle
    """

    def __init__(self):
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

    def card_count(self):
        return len(self.generated_deck)

    def draw(self):
        return self.generated_deck.pop(0)
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
