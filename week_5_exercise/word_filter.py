# Using comprehension, write a program that receives some text, separated by space,
# and takes only those words whose length is even.
# Print each word on a new line.

even_length_words = [word for word in input().split() if len(word) % 2 == 0]
print('\n'.join(even_length_words))