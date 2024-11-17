
card_deck = input().split(', ')
number_of_commands = int(input())

for command in range(number_of_commands):
    input_command = input().split(', ')
    if input_command[0] == 'Add':
        card_name = input_command[1]
        if card_name in card_deck:
            print("Card is already in the deck")
        else:
            print("Card successfully added")
            card_deck.append(card_name)
    elif input_command[0] == 'Remove':
        card_name = input_command[1]
        if card_name not in card_deck:
            print("Card not found")
        else:
            print("Card successfully removed")
            card_deck.remove(card_name)
    elif input_command[0] == 'Remove At':
        card_index = int(input_command[1])
        if 0 <= card_index <= len(card_deck) - 1:
            print("Card successfully removed")
            card_deck.pop(card_index)
        else:
            print("Index out of range")
    elif input_command[0] == 'Insert':
        card_index, card_name = int(input_command[1]), input_command[2]
        if card_index < 0 or card_index > len(card_deck) - 1:
            print("Index out of range")
        else:
            if card_name in card_deck:
                print("Card is already added")
            else:
                print('Card successfully added')
                card_deck.insert(card_index, card_name)

print(*card_deck, sep=', ')
