# Write a program that reads a single string with numbers separated by comma and space ", ".
# Print the indices of all even numbers.

input_string = [int(number) for number in input().split(', ')]
even_numbers = [index for index, number in enumerate(input_string) if number % 2 == 0]
print(even_numbers)