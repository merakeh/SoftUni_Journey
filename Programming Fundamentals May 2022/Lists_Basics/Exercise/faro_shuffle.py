deck_of_cards = input().split()
count_of_shuffles = int(input())
shuffled_deck = []
for shuffle in range(count_of_shuffles):
    middle_of_deck = len(deck_of_cards) // 2
    first_half = deck_of_cards[0:middle_of_deck]
    second_half = deck_of_cards[middle_of_deck::]
    shuffled_deck = []
    for index in range(len(first_half)):
        shuffled_deck.append(first_half[index])
        shuffled_deck.append(second_half[index])
    deck_of_cards = shuffled_deck

print(shuffled_deck)





# for index in range(len(deck_of_cards)):
#     if index < len(deck_of_cards) / 2:
#         first_half.append(deck_of_cards[index])
#     else:
#         second_half.append(deck_of_cards[index])
#
# for i in range(len(first_half)):
#     shuffled_deck.append(first_half[i])
#     shuffled_deck.append(second_half[i])
#
# print(shuffled_deck)
