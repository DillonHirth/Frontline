class Hand:
    """Hand class, owned by player. Deck needs to be instantiated first

    Methods:
        sort
        play_card
    """

    def __init__(self, player_main_deck, starting_hand_point_value):
        self.hand_value = 0
        self.hand = self.draw_main_to_point_value(player_main_deck, starting_hand_point_value)

    # def __repr__(self):
    #     return None

    def draw_main_to_point_value(self, player_main_deck, point_value):
        hand = []
        while self.hand_value < point_value:
            card = player_main_deck.draw()
            self.hand_value += card.value
            hand.append(card)
        return hand

    ##CardCount()
    ##PointCount()
    ##PlayCard()
