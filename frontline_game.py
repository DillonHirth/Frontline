"""
deck:
    deck generator/manipulator class
"""

from player import Player

suit_list = ['Spade', 'Diamond', 'Club', 'Heart']
numerical_value_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
face_value_list = ['Jack', 'Queen', 'King', 'Ace', 'Joker']
# d = Deck(suit_list, numerical_value_list)
# print(d)
# d.shuffle()
# print(d)
#
# s = Deck(suit_list, face_value_list)
# print(s)
# s.shuffle()
# print(s)

player = Player("Steve")
player_hand = player.player_starting_hand.hand

count = 0
for card in player_hand:
    count += card.value
    print(card.value)
print(count)
