sequence_of_elements = [element for element in input().split()]
moves = 0

while True:
    input_command = input().split()
    if input_command[0] == 'end':
        print("Sorry you lose :(")
        print(*sequence_of_elements)
        break
    moves += 1
    index_one, index_two = int(input_command[0]), int(input_command[1])
    is_input_valid = (index_one != index_two and 0 <= index_one <= len(sequence_of_elements) - 1 and 0 <= index_two <= len(sequence_of_elements) - 1)
    if is_input_valid:
        if sequence_of_elements[index_one] == sequence_of_elements[index_two]:
            print(f"Congrats! You have found matching elements - {sequence_of_elements[index_one]}!")
            value_to_remove = sequence_of_elements[index_one]
            sequence_of_elements.remove(value_to_remove)
            sequence_of_elements.remove(value_to_remove)
            if not sequence_of_elements:
                print(f"You have won in {moves} turns!")
                break
        else:
            print("Try again!")
    else:
        print('Invalid input! Adding additional elements to the board')
        middle_index = int(len(sequence_of_elements) / 2)
        sequence_of_elements[middle_index:middle_index] = [f"-{moves}a", f"-{moves}a"]



