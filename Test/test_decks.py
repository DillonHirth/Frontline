"""
random:
    https://docs.python.org/3/library/random.html
"""
from ..decks import Deck

suit_list = ['Spade', 'Diamond', 'Club', 'Heart']
numerical_value_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
face_value_list = ['Jack', 'Queen', 'King', 'Ace', 'Joker']
value_range = range(2, 11)

main_deck_test = Deck(suit_list, numerical_value_list)
support_deck_test = Deck(suit_list, face_value_list)


def test_maindeck_value_and_suit():
    """pops the first card off of the deck and returns it"""

    for item in main_deck_test.generated_deck:
        assert item.value in value_range and item.suit in suit_list


def test_maindeck_decks_card_count():
    """pops the first card off of the deck and returns it"""

    assert main_deck_test.card_count() == 36


def test_maindeck_decks_draw():
    """pops the first card off of the deck and returns it"""

    card = main_deck_test.draw()
    assert card.value in value_range and card.suit in suit_list and \
           main_deck_test.card_count() == 35


def test_support_value_and_suit():
    """pops the first card off of the deck and returns it"""

    for item in support_deck_test.generated_deck:
        assert item.value in face_value_list and item.suit in suit_list


def test_support_decks_card_count():
    """pops the first card off of the deck and returns it"""

    assert support_deck_test.card_count() == 20


def test_support_decks_draw():
    """pops the first card off of the deck and returns it"""

    card = support_deck_test.draw()
    assert card.value in face_value_list and card.suit in suit_list and \
           support_deck_test.card_count() == 19
