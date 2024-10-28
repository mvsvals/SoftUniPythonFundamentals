# Input
# On the first line, you will receive integers separated by "|" representing the targets in the archery field.
# On the next lines, until the "Game over" command, you will receive commands in the format described above.
# Output
# Print the field in the following format:
# "{target} - {target} - {target} - … - {target}"
#
# "John finished the archery tournament with {points} points!"


integer_list = [int(number) for number in input().split('|')]
total_points = 0

while True:
    input_string = input()
    if input_string == 'Game over':
        break
    input_command = input_string.split('@')
    if input_command[0] == 'Shoot Left':
        start_index = int(input_command[1])
        length = int(input_command[2])
        if 0 <= start_index <= len(integer_list) - 1:
            destination_index = start_index - length
            if abs(destination_index) > len(integer_list) - 1:
                destination_index = destination_index % len(integer_list)
            if integer_list[destination_index] < 5:
                total_points += integer_list[destination_index]
                integer_list[destination_index] = 0
            else:
                integer_list[destination_index] -= 5
                total_points += 5
    elif input_command[0] == 'Shoot Right':
        start_index = int(input_command[1])
        length = int(input_command[2])
        if 0 <= start_index <= len(integer_list) - 1:
            destination_index = start_index + length
            if destination_index > len(integer_list) - 1:
                destination_index = destination_index % len(integer_list)
            if integer_list[destination_index] < 5:
                total_points += integer_list[destination_index]
                integer_list[destination_index] = 0
            else:
                integer_list[destination_index] -= 5
                total_points += 5


    elif input_command[0] == 'Reverse':
        integer_list = integer_list[::-1]

print(*integer_list, sep=' - ')
print(f'John finished the archery tournament with {total_points} points!')