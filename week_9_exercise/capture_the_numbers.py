# Write a program that receives strings on different lines and extracts only the numbers.
# Print all extracted numbers on a single line, separated by a single space.
import re

string = input()
pattern = r'\d+'
match_list = []

while string:
    match = re.findall(pattern, string)
    match_list += match
    string = input()

print(' '.join(match_list))
