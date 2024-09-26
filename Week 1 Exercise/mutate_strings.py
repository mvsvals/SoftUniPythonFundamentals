# You will be given two strings.
# Transform the first string into the second one, letter by letter, starting from the first one.
# After each interaction, print the resulting string only if it is unique.
# Note: the strings will have the same length.


first_string = input()
second_string = input()

previous_string = first_string
current_string = ''

for character_position in range(len(first_string)):
    current_string = second_string[:character_position + 1] + first_string[character_position + 1:]
    if current_string != previous_string:
        print(current_string)
        previous_string = current_string








