
initial_array = [int(number) for number in input().split()]
modified_array = initial_array


while True:
    input_command_string = input().split()
    input_command = input_command_string[0]
    if input_command == 'end':
        break
    elif input_command == 'swap':
        index_one, index_two = int(input_command_string[1]), int(input_command_string[2])
        modified_array[index_one], modified_array[index_two] = modified_array[index_two], modified_array[index_one]
    elif input_command == 'multiply':
        index_one, index_two = int(input_command_string[1]), int(input_command_string[2])
        modified_array[index_one] *= modified_array[index_two]
    elif input_command == 'decrease':
        modified_array = list(map(lambda x: x - 1, modified_array))

print(*modified_array, sep=", ")

