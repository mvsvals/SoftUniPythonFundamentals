input_number = input().split()
input_string = list(input())
final_text = []

for number in input_number:
    sum_of_number = sum(int(digit) for digit in number)
    position = sum_of_number % len(input_string)
    final_text.append(input_string[position])
    input_string.pop(position)

print(''.join(final_text))