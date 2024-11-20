
import re

mirror_words = []
total_matches = 0

input_string = input()

pattern = r'(#|@)([a-zA-Z]{3,})\1{2}([a-zA-Z]{3,})\1'
matches = re.findall(pattern, input_string)


if not matches:
    print("No word pairs found!")
else:
    for match in matches:
        total_matches += 1
        first_word, second_word = match[1:]
        if first_word == second_word[::-1] and first_word[::-1] == second_word:
            mirror_words.append(f'{first_word} <=> {second_word}')
    print(f'{total_matches} word pairs found!')

if not mirror_words:
    print('No mirror words!')
else:
    print('The mirror words are:')
    print(', '.join(mirror_words))




