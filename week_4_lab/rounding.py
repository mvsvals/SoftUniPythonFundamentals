# Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list.
# Use round().

input_numbers = [round(float(number)) for number in input().split()]
print(input_numbers)
