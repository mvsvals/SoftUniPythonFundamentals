# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print the min and max values of the given numbers and the sum of all the numbers in the list. Use min(), max() and sum().
# The output should be as follows:
#     • On the first line: "The minimum number is {minimum number}"
#     • On the second line: "The maximum number is {maximum number}"
#     • On the third line: "The sum number is: {sum of all numbers}"

def calculation(number_list: list) -> str:
    return f'The minimum number is {min(number_list)}\nThe maximum number is {max(number_list)}\nThe sum number is: {sum(number_list)}'

input_numbers = [int(num) for num in input().split()]
print(calculation(input_numbers))



