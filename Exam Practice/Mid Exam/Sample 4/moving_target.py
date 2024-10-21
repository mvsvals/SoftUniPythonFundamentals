
integer_sequence = [int(number) for number in input().split()]

while True:
    input_command = input().split()
    if 'End' in input_command:
        break
    index = int(input_command[1])
    if 'Shoot' in input_command:
        power = int(input_command[2])
        if 0 <= index <= len(integer_sequence) - 1:
            integer_sequence[index] -= power
            if integer_sequence[index] <= 0:
                integer_sequence.pop(index)
    elif 'Add' in input_command:
        value = int(input_command[2])
        if 0 <= index <= len(integer_sequence) - 1:
            integer_sequence.insert(index, value)
        else:
            print('Invalid placement!')
    elif 'Strike' in input_command:
        radius = int(input_command[2])
        left_side = integer_sequence[:index]
        right_side = integer_sequence[index + 1:]
        if len(left_side) < radius or len(right_side) < radius or len(integer_sequence) - 1 < index:
            print("Strike missed!")
        else:
            integer_sequence[index - radius: index + radius + 1] = []


print(*integer_sequence, sep='|')