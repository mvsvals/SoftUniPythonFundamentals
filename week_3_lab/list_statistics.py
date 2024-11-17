# On the first line, you will receive a number n.
# On the following n lines, you will receive integers. You should create and print two lists:
#     • One with all the positive (including 0) numbers
#     • One with all the negative numbers
# Finally, print the following message:
# "Count of positives: {count_positives}
# Sum of negatives: {sum_of_negatives}"

input_number = int(input())
positive_numbers_list, negative_numbers_list = [], []
sum_of_negatives = 0

for _ in range(input_number):
    integer_input = int(input())
    if integer_input >= 0:
        positive_numbers_list.append(integer_input)
    else:
        negative_numbers_list.append(integer_input)

print(positive_numbers_list)
print(negative_numbers_list)


print(f'Count of positives: {len(positive_numbers_list)}')
print(f'Sum of negatives: {sum(negative_numbers_list)}')