# You will be given a number. Print the largest number that can be formed from the digits of the given number.

# Examples
# Input   Output
# 213     321
# 7389    9873



input_number = int(input())
number_string = str(input_number)

largest_number_list = sorted(number_string, reverse=True)
largest_number_string = ''.join(largest_number_list)

print(largest_number_string)


















