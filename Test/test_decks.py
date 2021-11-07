from ..decks import *


def test_value_between_two_and_ten():
    assert Card(10, "heart").value in range(1, 11)

def test_generate_deck_count():
    d = MainDeck()
    assert len(d.generated_deck) == 36
