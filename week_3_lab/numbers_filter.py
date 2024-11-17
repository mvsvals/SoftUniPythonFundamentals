# On the first line, you will receive a single number n.
# On the following n lines, you will receive integers.
# After that, you will be given one of the following commands:
#     • even
#     • odd
#     • negative
#     • positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.


input_number = int(input())
integer_list = []
output_list = []

for _ in range(input_number):
    input_integer = int(input())
    integer_list.append(input_integer)

input_command = input()

for element in integer_list:
    if input_command == 'even':
        if element % 2 == 0:
            output_list.append(element)
    elif input_command == 'odd':
        if element % 2 != 0:
            output_list.append(element)
    elif input_command == 'negative':
        if element < 0:
            output_list.append(element)
    elif input_command == 'positive':
        if element >= 0:
            output_list.append(element)
print(output_list)


