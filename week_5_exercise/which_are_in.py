# You will be given two sequences of strings, separated by ", ".
# Print a new list containing only the strings from the first input line, which are substrings of any string in the second input line.

string_sequences_one = input().split(', ')
string_sequences_two = input().split(', ')
list_final = []

for string_one in string_sequences_one:
    for string_two in string_sequences_two:
        if string_one in string_two:
            list_final.append(string_one)
            break

print(list_final)