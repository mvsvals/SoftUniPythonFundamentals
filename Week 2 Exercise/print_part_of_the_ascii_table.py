# Write a program that prints part of the ASCII table characters on the console, separated by a single space.
# On the first line of input, you will receive the char index you should start with.
# On the second line - the index of the last character you should print.

character_index_beginning = int(input())
character_index_end = int(input())
final_string = chr(character_index_beginning)

for i in range(character_index_beginning + 1, character_index_end + 1):
    final_string += " " + chr(i)
print(final_string)