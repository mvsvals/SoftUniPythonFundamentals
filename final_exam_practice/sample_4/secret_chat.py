
concealed_message = input()

while True:
    input_string = input()
    if input_string == 'Reveal':
        break
    command = input_string.split(':|:')[0]
    if command == 'InsertSpace':
        index = int(input_string.split(':|:')[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)
    elif command == 'Reverse':
        substring = input_string.split(':|:')[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, '', 1)
            concealed_message += substring[::-1]
            print(concealed_message)
        else:
            print('error')
    elif command == 'ChangeAll':
        substring, replacement = input_string.split(':|:')[1], input_string.split(':|:')[2]
        concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)

print(f"You have a new text message: {concealed_message}")

