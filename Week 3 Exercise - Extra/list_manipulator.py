initial_list = list(map(int, input().split()))

while True:
    input_command = input().split()

    if input_command[0] == 'end':
        break

    if input_command[0] == 'exchange':
        split_after_index = int(input_command[1])
        if split_after_index < 0 or split_after_index >= len(initial_list):
            print('Invalid index')
        else:
            new_list = initial_list[split_after_index + 1:] + initial_list[:split_after_index + 1]
            initial_list = new_list

    elif input_command[0] == 'max':
        if input_command[1] == 'even':
            max_even_number_list = [even_number for even_number in initial_list if even_number % 2 == 0]
            if not max_even_number_list:
                print('No matches')
            else:
                max_even_number = max(max_even_number_list)
                right_index = len(initial_list) - 1 - initial_list[::-1].index(max_even_number)
                print(right_index)
        elif input_command[1] == 'odd':
            max_odd_number_list = [odd_number for odd_number in initial_list if odd_number % 2 != 0]
            if not max_odd_number_list:
                print('No matches')
            else:
                max_odd_number = max(max_odd_number_list)
                right_index = len(initial_list) - 1 - initial_list[::-1].index(max_odd_number)
                print(right_index)

    elif input_command[0] == 'min':
        if input_command[1] == 'even':
            min_even_number_list = [even_number for even_number in initial_list if even_number % 2 == 0]
            if not min_even_number_list:
                print('No matches')
            else:
                min_even_number = min(min_even_number_list)
                right_index = len(initial_list) - 1 - initial_list[::-1].index(min_even_number)
                print(right_index)
        elif input_command[1] == 'odd':
            min_odd_number_list = [odd_number for odd_number in initial_list if odd_number % 2 != 0]
            if not min_odd_number_list:
                print('No matches')
            else:
                min_odd_number = min(min_odd_number_list)
                right_index = len(initial_list) - 1 - initial_list[::-1].index(min_odd_number)
                print(right_index)

    elif input_command[0] == 'first':
        count = int(input_command[1])
        if count > len(initial_list):
            print('Invalid count')
        elif input_command[2] == 'even':
            even_number_list = []
            for number in initial_list:
                if len(even_number_list) == count:
                    break
                if number % 2 == 0:
                    even_number_list.append(number)
            print(even_number_list)
        elif input_command[2] == 'odd':
            odd_number_list = []
            for number in initial_list:
                if len(odd_number_list) == count:
                    break
                if number % 2 != 0:
                    odd_number_list.append(number)
            print(odd_number_list)

    elif input_command[0] == 'last':
        count = int(input_command[1])
        if count > len(initial_list):
            print('Invalid count')
        elif input_command[2] == 'even':
            even_number_list = []
            for number in reversed(initial_list):
                if len(even_number_list) == count:
                    break
                if number % 2 == 0:
                    even_number_list.append(number)
            print(list(reversed(even_number_list)))
        elif input_command[2] == 'odd':
            odd_number_list = []
            for number in reversed(initial_list):
                if len(odd_number_list) == count:
                    break
                if number % 2 != 0:
                    odd_number_list.append(number)
            print(list(reversed(odd_number_list)))


print(f"[{', '.join(map(str, initial_list))}]")
