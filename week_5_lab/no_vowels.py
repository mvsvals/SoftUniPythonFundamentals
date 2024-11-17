# Using comprehension, write a program that receives a text and removes all its vowels, case insensitive.
# Print the new text string after removing the vowels. The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.

text_input = input()
print(''.join([letter for letter in text_input if letter.lower() not in ['a', 'o', 'u', 'e', 'i']]))
