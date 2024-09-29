# A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half.
# Then the cards in the two halves are perfectly interleaved, such that the original bottom card is still on the bottom and the original top card is still on top.
# For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six']
# Write a program that receives a single string (cards separated by space) and on the second line receives a count of faro shuffles that should be made. Print the state of the deck after the shuffle.
# Note: The length of the deck of cards will always be an even number.

input_cards = input().split()
shuffle_counts = int(input())

for shuffle in range(shuffle_counts):
    middle_of_the_deck = len(input_cards) // 2
    left_side_of_the_deck = input_cards[:middle_of_the_deck]
    right_side_of_the_deck = input_cards[middle_of_the_deck:]
    shuffled_deck = []
    for card_index in range(len(left_side_of_the_deck)):
        shuffled_deck.append(left_side_of_the_deck[card_index])
        shuffled_deck.append(right_side_of_the_deck[card_index])
    input_cards = shuffled_deck

print(input_cards)
