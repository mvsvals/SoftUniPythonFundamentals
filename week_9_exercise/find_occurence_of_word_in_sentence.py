# Write a program that finds how many times a word is used in a string.
# The output is a single number indicating the number of times the string contains the word.
# Note that letter case does not matter – it is case-insensitive.

import re

input_string = input()
word_to_count = fr'\b{input()}\b'

matches = re.findall(word_to_count, input_string, re.IGNORECASE)
print(len(matches))