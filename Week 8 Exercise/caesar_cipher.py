# Write a program that returns an encrypted version of the same text.
# Encrypt the text by replacing each character with the corresponding character three positions forward in the ASCII table.
# For example, A would be replaced with D, B would become E, and so on. Print the encrypted text.

raw_text = input()
encrypted_text = ''

for char in raw_text:
    char_ascii_value = ord(char)
    char_ascii_value += 3
    encrypted_text += str(chr(char_ascii_value))

print(encrypted_text)