from decks import MainDeck as MainDeck
from decks import SupportDeck as SupportDeck

d = MainDeck()
print(d)
d.shuffle()
print(d)

d = SupportDeck()
print(d)
d.shuffle()
print(d)

