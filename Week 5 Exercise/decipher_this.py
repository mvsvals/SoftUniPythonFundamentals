# You are given a secret message you should decipher. To do that, you need to know that in each word:
#     • the second and the last letter are switched (e.g., Holle means Hello)
#     • the first letter is replaced by its character code (e.g., 72 means H)

secret_message = input().split()

for word in secret_message:
    word_list = list(word)
    digit_part = [char for char in word_list if char.isdigit()]
    letter_part = [char for char in word_list if char.isalpha()]
    digit_part = ''.join(digit_part)
    digit_part = chr(int(digit_part))
    second_letter = letter_part[0]
    last_letter = letter_part[-1]
    letter_part[0] = last_letter
    letter_part[-1] = second_letter
    print(digit_part + ''.join(letter_part), end=' ')
