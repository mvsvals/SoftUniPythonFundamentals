# On the first line, you will receive a string. On the second line, you will receive a second string.
# Write a program that removes all the occurrences of the first string in the second until there is no match.
# At the end, print the remaining string.

string_one = input()
string_two = input()

while string_one in string_two:
    string_two = string_two.replace(string_one, '')

print(string_two)