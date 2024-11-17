# A palindrome is a number that reads the same backward as forward, such as 323 or 1001.
# Write a function that receives a list of positive integers, separated by comma and space ", ".
# The function should check if each integer is a palindrome - True or False. Print the result.
def palindrome_check(numbers_list: list) -> str:
    results = []
    for number in numbers_list:
        if number[::-1] == number:
            results.append('True')
        else:
            results.append('False')
    return results


input_numbers = [num for num in input().split(', ')]
print('\n'.join(palindrome_check(input_numbers)))