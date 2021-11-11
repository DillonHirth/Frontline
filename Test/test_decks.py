from ..decks import *

main_deck_test = MainDeck()
support_deck_test = SupportDeck()

suit_list = ['Spade', 'Diamond', 'Club', 'Heart']
value_list = ['Jack', 'Queen', 'King', 'Ace', 'Joker']
value_range = range(2, 11)


def test_maindeck_value_and_suit():
    for item in main_deck_test.generated_deck:
        assert item.value in range(2, 11) and item.suit in ['Spade', 'Diamond', 'Club', 'Heart']


def test_maindeck_decks_card_count():
    assert main_deck_test.card_count() == 36


def test_maindeck_decks_draw():
    card = main_deck_test.draw()
    assert card.value in value_range and card.suit in suit_list and main_deck_test.card_count() == 35


def test_supportdeck_value_and_suit():
    for item in support_deck_test.generated_deck:
        assert item.value in value_list and item.suit in suit_list


def test_supportdeck_decks_card_count():
    assert support_deck_test.card_count() == 20


def test_supportdeck_decks_draw():
    card = support_deck_test.draw()
    assert card.value in value_list and card.suit in suit_list and support_deck_test.card_count() == 19
