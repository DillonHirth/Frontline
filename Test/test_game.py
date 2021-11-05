from ..decks import *


def test_value_between_two_and_ten():
    assert Card(10, "heart").value in range(1, 11)
