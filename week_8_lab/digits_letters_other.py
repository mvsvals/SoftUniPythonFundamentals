# Write a program that receives a single string.
# On the first line, print all the digits found in the string, on the second – all the letters, and on the third – all the other characters.
# There will always be at least one digit, one letter, and one other character.

input_string = input()

first_line = [digit for digit in input_string if digit.isdigit()]
second_line = [alpha for alpha in input_string if alpha.isalpha()]
third_line = [other for other in input_string if not other.isalnum()]

print(''.join(first_line))
print(''.join(second_line))
print(''.join(third_line))