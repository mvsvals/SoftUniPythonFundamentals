number_sequence = [int(number) for number in input().split()]

while True:
    input_command = input()
    if input_command == 'Finish':
        break
    command = input_command.split()[0]
    value = int(input_command.split()[1])
    if command == 'Add':
        number_sequence.append(value)
    elif command == 'Remove' and value in number_sequence:
        number_sequence.remove(value)
    elif command == 'Replace' and value in number_sequence:
        replacement = input_command.split()[2]
        index = number_sequence.index(value)
        number_sequence[index] = replacement
    elif command == 'Collapse':
        number_sequence = list(filter(lambda x: x >= value, number_sequence))

print(*number_sequence)
