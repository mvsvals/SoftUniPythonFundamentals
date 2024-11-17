# Write a program that counts all characters in a string except for space (" ").
#
# Print all the occurrences in the following format:
#
# "{char} -> {occurrences}"


input_string = input()
count_dict = {}

for char in input_string:
    if char == " ":
        continue
    count_dict[char] = input_string.count(char)

for key, value in count_dict.items():
    print(f'{key} -> {value}')
