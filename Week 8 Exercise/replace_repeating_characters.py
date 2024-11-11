# Write a program that reads a string from the console and replaces any sequence of the same letters with a single corresponding letter.

input_string = input()
previous_char = None
output_string = ''

for char in input_string:
    if char == previous_char:
        continue
    previous_char = char
    output_string += previous_char

print(output_string)