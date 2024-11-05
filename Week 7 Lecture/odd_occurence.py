# Write a program that prints all elements from a given sequence of words that occur an odd number of times (case-insensitive) in it.
#     • Words are given on a single line, space-separated.
#     • Print the result elements in lowercase, in their order of appearance.


def find_odd_number_of_string_occurence(input_list: list):
    sample_dict = {}
    for string in input_list:
        if string in sample_dict:
            sample_dict[string] += 1
        else:
            sample_dict[string] = 1
    for key, value in sample_dict.items():
        if value % 2 != 0:
            print(key, end=' ')


input_sequence = input().lower().split()
find_odd_number_of_string_occurence(input_sequence)
