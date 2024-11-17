# Write a function that receives two integer numbers. Calculate the factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.

def factorial_calculation(num1: int, num2: int) -> int:
    factorial_one = num1
    factorial_two = num2
    for num in range(num1 - 1, 0, -1):
        factorial_one *= num
    for num in range(num2 - 1, 0, -1):
        factorial_two *= num
    return f'{factorial_one / factorial_two:.2f}'

number_one = int(input())
number_two = int(input())

print(factorial_calculation(number_one, number_two))