
input_string = input()

while True:
    input_command = input().split()
    if input_command[0] == 'Done':
        break
    if input_command[0] == 'TakeOdd':
        input_string = [char for index, char in enumerate(input_string) if index % 2 != 0]
        input_string = ''.join(input_string)
        print(input_string)
    elif input_command[0] == 'Cut':
        index, length = int(input_command[1]), int(input_command[2])
        substring = input_string[index:index + length]
        input_string = input_string.replace(substring, '', 1)
        print(input_string)
    elif input_command[0] == 'Substitute':
        substring, substitute = input_command[1:]
        if substring in input_string:
            input_string = input_string.replace(substring, substitute)
            print(input_string)
        else:
            print('Nothing to replace!')

print(f'Your password is: {input_string}')