# You receive a string consisting of a number between two letters.
# For the given string, you should perform different mathematical operations to achieve a result:
#     • First, if the letter in front of the number is:
#         ◦ Uppercase: divide the number by the letter's position in the alphabet (starting from 1)
#         ◦ Lowercase: multiply the number with the letter's position in the alphabet (starting from 1)
#     • Next, if the letter after the number is:
#         ◦ Uppercase: subtract its position from the resulting number (starting from 1)
#         ◦ Lowercase: add its position to the resulting number (starting from 1)
# The game was too easy for John. He decided to complicate it by doing the same calculations to multiple strings keeping track of only the total sum of all results.
# Once he started to solve this with more strings and bigger numbers, it became quite hard to do it only in his mind.
# He kindly asks you to write a program that performs the operations described above and sums the final results of each string.

# Output
#     • Print at the console a single number:
#         ◦ The total sum of all processed numbers, formatted to the second decimal separator
# Constraints
#     • The count of the strings will be in the range [1 … 10]
#     • The numbers between the letters will be integers in the range [1 … 2 147 483 647]
#     • Time limit: 0.3 sec. Memory limit: 16 MB


input_string = input().split()
total_sum = 0

for string in input_string:
    result = 0
    first_letter = string[0]
    number = int(string[1:-1])
    second_letter = string[-1]

    first_letter_position = ord(first_letter.lower()) - ord('a') + 1
    second_letter_position = ord(second_letter.lower()) - ord('a') + 1

    if first_letter.isupper():
        result = number / first_letter_position
    else:
        result = number * first_letter_position
    if second_letter.isupper():
        result -= second_letter_position
    else:
        result += second_letter_position

    total_sum += result

print(f'{total_sum:.2f}')


