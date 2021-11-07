from ..decks import *

d = MainDeck()


def test_value_between_two_and_ten():
    for item in d.generated_deck:
        assert item.value in range(2, 11) and item.suit in ['Spade', 'Diamond', 'Club', 'Heart']


def test_generate_deck_count():
    assert len(d.generated_deck) == 36
