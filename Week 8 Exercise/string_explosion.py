input_string = list(input())
index = 0
total_strength_remaining = 0

while index < len(input_string):
    current_char = input_string[index]

    if current_char == '>':
        total_strength_remaining += int(input_string[index + 1])
        index += 1

    elif total_strength_remaining > 0:
        input_string.pop(index)
        index += 1

    else:
        index += 1

print(''.join(input_string))