input_numbers = list(map(int, input().split(', ')))

for number in input_numbers:
    if number == 0:
        input_numbers.remove(0)
        input_numbers.append(number)

print(input_numbers)
