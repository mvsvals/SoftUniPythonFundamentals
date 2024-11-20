
initial_string = list(input())

while True:
    input_string = input()
    if input_string == 'Travel':
        break
    command, val1, val2 = input_string.split(':')
    if command == 'Add Stop':
        index = int(val1)
        string = val2
        if 0 <= index < len(initial_string):
            initial_string = initial_string[:index] + list(string) + initial_string[index:]
        print(*initial_string, sep='')
    elif command == 'Remove Stop':
        start_index = int(val1)
        end_index = int(val2)
        if 0 <= start_index <= end_index < len(initial_string):
            del initial_string[start_index:end_index+1]
        print(*initial_string, sep='')
    elif command == 'Switch':
        old_string = val1
        new_string = val2
        if old_string in ''.join(initial_string):
            work_string = ''.join(initial_string).replace(old_string, new_string)
            initial_string = list(work_string)
        print(*initial_string, sep='')

print(f"Ready for world tour! Planned stops: ", end='')
print(*initial_string, sep='')
