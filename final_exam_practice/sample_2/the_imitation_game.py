
encrypted_message = list(input())

while True:
    input_string = input()
    if input_string == 'Decode':
        break
    command = input_string.split('|')[0]
    if command == 'Move':
        total_letters = int(input_string.split('|')[1])
        part_to_move = encrypted_message[:total_letters]
        encrypted_message = encrypted_message[total_letters:] + part_to_move
    elif command == 'Insert':
        index = int(input_string.split('|')[1])
        value = input_string.split('|')[2]
        encrypted_message[index:index] = list(value)
    elif command == 'ChangeAll':
        substring = input_string.split('|')[1]
        replacement = input_string.split('|')[2]
        encrypted_message = list(''.join(encrypted_message).replace(substring, replacement))


print(f'The decrypted message is: ', end='')
print(''.join(encrypted_message))
