import decks as deck


def test_value_between_two_and_ten():
    assert deck.Card(10, "heart").value in range(1, 11)
