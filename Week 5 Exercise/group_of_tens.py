# Write a program that receives a sequence of numbers (a string containing integers separated by ", ") and
# prints the numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
# Examples:
#     • The numbers 2, 8, 4, and 10 fall into the group of 10's.
#     • The numbers 13, 19, 14, and 15 fall into the group of 20's.
# For more clarification, see the examples below.

input_sequence = [int(number) for number in input().split(', ')]

current_group = 10

while input_sequence:
    current_list = [number for number in input_sequence if number <= current_group]
    for i in current_list:
        input_sequence.remove(i)
    print(f'Group of {current_group}s: {current_list}')
    current_group += 10





