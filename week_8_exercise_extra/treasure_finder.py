# Write a program that decrypts a message by a given key and gathers information about hidden treasure type and its coordinates.
# On the first line, you will receive a key (sequence of numbers separated by a space).
# On the next few lines, you will receive lines with strings until you get the command "find".
# You should loop through every string and decrease the ASCII code of each character with a corresponding number of the key sequence.
# You choose a key number from the sequence by just looping through it.
# If the length of the key sequence is less than the string sequence, you should continue looping from the beginning.
# For more clarification, see the example below.
# After decrypting the message, you will get a type of treasure and its coordinates. The type will be between the symbol "&", and the coordinates - between the symbols "<' and '>'.
# For each line print the type and the coordinates in the format "Found {type} at {coordinates}".


input_key = [int(number) for number in input().split()]


while True:
    input_string = input()
    index = 0
    if input_string == 'find':
        break
    decrypted_string = ''
    for char in input_string:
        if index >= len(input_key):
            index = 0
        new_char_ascii = ord(char) - input_key[index]
        decrypted_string += chr(new_char_ascii)
        index += 1
    type_start_index = decrypted_string.find('&')
    type_end_index = decrypted_string.find('&', type_start_index + 1)
    coord_start_index = decrypted_string.find('<')
    coord_end_index = decrypted_string.find('>')
    type = decrypted_string[type_start_index + 1:type_end_index]
    coordinates = decrypted_string[coord_start_index + 1:coord_end_index]
    print(f"Found {type} at {coordinates}")

