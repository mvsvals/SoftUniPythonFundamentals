
number_of_pieces = int(input())
piano_pieces_dict = {}

for x in range(number_of_pieces):
     piece, composer, key = input().split('|')
     piano_pieces_dict[piece] = [composer, key]

while True:
    input_string = input()
    if input_string == 'Stop':
        break
    command_string = input_string.split('|')
    if command_string[0] == 'Add':
        piece, composer, key = command_string[1:]
        if not piece in piano_pieces_dict:
            piano_pieces_dict[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f'{piece} is already in the collection!')
    elif command_string[0] == 'Remove':
        piece = command_string[1]
        if piece in piano_pieces_dict:
            piano_pieces_dict.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command_string[0] == 'ChangeKey':
        piece, new_key = command_string[1:]
        if piece in piano_pieces_dict:
            piano_pieces_dict[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, info in piano_pieces_dict.items():
    print(f"{piece} -> Composer: {info[0]}, Key: {info[1]}")