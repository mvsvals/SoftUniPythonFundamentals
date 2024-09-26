# You will be given the number n. After that, you'll receive different strings n times.
# Strings are pure, meaning that they do NOT consist of any of the characters: comma ",", period ".", or underscore "_":
#     • If a string is pure, print "{string} is pure."
#     • Otherwise, print "{string} is not pure!"

number_of_strings = int(input())

for i in range(number_of_strings):
    input_string = input()
    if ("," in input_string or
            "." in input_string or
            "_" in input_string):
        print(f'{input_string} is not pure!')
    else:
        print(f'{input_string} is pure.')
