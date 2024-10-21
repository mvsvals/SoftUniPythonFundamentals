# Using a list comprehension, write a program that receives numbers, separated by comma and space ", ", and
# prints all the positive, negative, even, and odd numbers on separate lines as shown below.
# Note: Zero is counted as a positive number


input_list = input().split(', ')
positive_numbers = [number for number in input_list if int(number) >= 0]
negative_numbers = [number for number in input_list if int(number) < 0]
even_numbers = [number for number in input_list if int(number) % 2 == 0]
odd_numbers = [number for number in input_list if int(number) % 2 != 0]

print('Positive: ' + ', '.join(positive_numbers))
print('Negative: ' + ', '.join(negative_numbers))
print('Even: ' + ', '.join(even_numbers))
print('Odd: ' + ', '.join(odd_numbers))
