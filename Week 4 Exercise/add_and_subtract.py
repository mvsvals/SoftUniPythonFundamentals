# You will receive three integer numbers.
# Write functions named:
#     • sum_numbers() that returns the sum of the first two integers
#     • subtract() that returns the difference between the returned result of the first function and the third integer
# Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters.
# Print the result of the subtract() function on the console.




def add_and_subtract(num1: int, num2: int, num3: int) -> int:
    def sum_numbers(num1: int, num2: int) -> int:
        return num1 + num2

    def subtract():
        return (sum_numbers(num1, num2)) - num3

    return subtract()

integer_one = int(input())
integer_two = int(input())
integer_three = int(input())

print(add_and_subtract(integer_one, integer_two, integer_three))


