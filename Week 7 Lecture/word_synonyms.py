# Write a program, which keeps a dictionary with synonyms.
# The key of the dictionary will be the word.
# The value will be a list of all the synonyms of that word.
# You will be given a number n – the count of the words.
# After each term, you will be given a synonym, so the count of lines you should read from the console is 2 * n.
# You will be receiving a word and a synonym each on a separate line like this:
#     • {word}
#     • {synonym}
# If you get the same word twice, just add the new synonym to the list.
# Print the words in the following format:
# {word} - {synonym1, synonym2 … synonymN}


word_count = int(input())
synonym_dictionary = {}

for word in range(word_count):
    input_key = input()
    input_value = input()
    if input_key in synonym_dictionary.keys():
        synonym_dictionary[input_key] += f', {input_value}'
    else:
        synonym_dictionary[input_key] = input_value

for key, value in synonym_dictionary.items():
    print(f'{key} - {value}')