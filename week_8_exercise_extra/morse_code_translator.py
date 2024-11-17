

input_morse_code_words = input().split(' | ')

morse_code_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z'
}

decrypted_message = []

for word in input_morse_code_words:
    letters = word.split()
    decrypted_word = ''
    for letter in letters:
        if letter in morse_code_dict:
            decrypted_word += morse_code_dict.get(letter)
    decrypted_message.append(decrypted_word)

print(' '.join(decrypted_message))