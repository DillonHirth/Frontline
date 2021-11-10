from ..decks import *

d = MainDeck()


def test_value_between_two_and_ten():
    for item in d.generated_deck:
        assert item.value in range(2, 11) and item.suit in ['Spade', 'Diamond', 'Club', 'Heart']


def test_decks_card_count():
    assert d.card_count() == 36


def test_decks_draw():
    card = d.draw()
    assert card.value in range(2, 11) and card.suit in ['Spade', 'Diamond', 'Club', 'Heart'] and d.card_count() == 35
