
original_card_deck = input().split(':')
new_card_deck = []

while True:
    input_string = input()
    if input_string == "Ready":
        break
    input_string = input_string.split()
    command = input_string[0]
    if command == 'Add':
        card_name = input_string[1]
        if card_name in original_card_deck:
            new_card_deck.append(card_name)
        else:
            print("Card not found.")
    elif command == 'Insert':
        card_name = input_string[1]
        index = int(input_string[2])
        if card_name in original_card_deck and 0 <= index <= len(new_card_deck) - 1:
            new_card_deck.insert(index, card_name)
        else:
            print("Error!")
    elif command == 'Remove':
        card_name = input_string[1]
        if card_name in new_card_deck:
            new_card_deck.remove(card_name)
        else:
            print("Card not found.")
    elif command == 'Swap':
        card_name_one = input_string[1]
        card_name_two = input_string[2]
        card_index_one = new_card_deck.index(card_name_one)
        card_index_two = new_card_deck.index(card_name_two)
        new_card_deck[card_index_one], new_card_deck[card_index_two] = new_card_deck[card_index_two], new_card_deck[card_index_one]
    elif command == 'Shuffle':
        new_card_deck = new_card_deck[::-1]


print(*new_card_deck)