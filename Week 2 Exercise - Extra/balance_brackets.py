
number_of_lines = int(input())
is_balanced = True
last_bracket = ''
are_brackets_opened = False

for i in range(number_of_lines):
    input_string = input()
    if last_bracket == input_string:
        is_balanced = False
    elif input_string == '(' and are_brackets_opened:
        is_balanced = False
    elif input_string == ')' and not are_brackets_opened:
        is_balanced = False
    elif input_string == '(':
        last_bracket = input_string
        are_brackets_opened = True
    elif input_string == ')':
        last_bracket = input_string
        are_brackets_opened = False

if is_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')



