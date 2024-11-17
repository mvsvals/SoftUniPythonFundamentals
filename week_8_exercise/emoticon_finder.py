# Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
# The input will be provided as a single string.

input_text = input()

for index in range(len(input_text)):
    if input_text[index] == ":":
        print(f':{input_text[index+1]}')
