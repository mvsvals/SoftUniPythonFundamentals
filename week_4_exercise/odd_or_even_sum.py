# You will receive a single number. You should write a function that returns the sum of all even and all odd digits in a given number.
# The result should be returned as a single string in the format:
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
# Print the result of the function on the console.

def sum_of_all_even_and_all_odd_digits(num: str) -> str:
    sum_of_odd_digits, sum_of_even_digits = 0, 0
    for digit in num:
        if int(digit) == 0:
            continue
        elif int(digit) % 2 == 0:
            sum_of_even_digits += int(digit)
        else:
            sum_of_odd_digits += int(digit)
    return f'Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}'


input_number = input()
print(sum_of_all_even_and_all_odd_digits(input_number))
