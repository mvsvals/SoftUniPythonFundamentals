# Write a program that takes a single string and prints a list of all the capital letters indices.
#
# Examples
# Input         Output
# pYtHoN        [1, 3, 5]
# CApiTAls      [0, 1, 4, 5]


input_string = input()
capital_list = []

for char_position in range(len(input_string)):
    if input_string[char_position].isupper():
        capital_list.append(char_position)

print(f'{capital_list}')
