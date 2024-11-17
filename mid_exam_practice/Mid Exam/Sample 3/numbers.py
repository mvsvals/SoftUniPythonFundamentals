# Write a program to read a sequence of integers and find and print the top 5 numbers greater than the average value in the sequence, sorted in descending order.

# Output
#     • Print the above-described numbers on a single line, space-separated.
#     • If less than 5 numbers hold the property mentioned above, print less than 5 numbers.
#     • Print "No" if no numbers hold the above property.
# Constraints
#     • All input numbers are integers in the range [-1 000 000 … 1 000 000].
#     • The count of numbers is in the range [1…10 000].


input_integers_sequence = [int(number) for number in input().split()]
average_value_of_sequence = sum(input_integers_sequence) / len(input_integers_sequence)

numbers_greater_than_average = [number for number in input_integers_sequence if number > average_value_of_sequence]
numbers_greater_than_average.sort(reverse=True)

if not numbers_greater_than_average:
    print('No')
else:
    print(' '.join(map(str, numbers_greater_than_average[:5])))
