
integer_sequence = [int(number) for number in input().split()]
targets_shot = 0


while True:
    input_command = input()
    if input_command == 'End':
        break
    shoot_index = int(input_command)
    if shoot_index > len(integer_sequence) - 1 or integer_sequence[shoot_index] < 0:
        continue
    else:
        last_value = integer_sequence[shoot_index]
        integer_sequence[shoot_index] = -1
        targets_shot += 1
        for index, number in enumerate(integer_sequence):
            if number < 0:
                continue
            elif number > last_value:
                integer_sequence[index] -= last_value
            elif number <= last_value:
                integer_sequence[index] += last_value




print("Shot targets: " + str(targets_shot) + " -> " + ' '.join([str(number) for number in integer_sequence]))

