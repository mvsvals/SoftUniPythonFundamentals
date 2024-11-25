
encrypted_message = input()


# A B C D
# 0 1 2 3

while True:
    input_string = input()
    if input_string == 'Decode':
        break
    command = input_string.split('|')
    if command[0] == 'Move':
        number_of_letters = int(command[1])
        encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]
    elif command[0] == 'Insert':
        index, value = int(command[1]), command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif command[0] == 'ChangeAll':
        substring, replacement = command[1:]
        encrypted_message = encrypted_message.replace(substring, replacement)

print(f"The decrypted message is: {encrypted_message}")