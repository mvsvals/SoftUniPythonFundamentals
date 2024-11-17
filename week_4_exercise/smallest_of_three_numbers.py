# Write a function that receives three integer numbers and returns the smallest.
# Print the result on the console. Use an appropriate name for the function.

def smallest_number_of_three(num1: int, num2: int, num3: int) -> int:
    return min(num1, num2, num3)

integer_one = int(input())
integer_two = int(input())
integer_three = int(input())

print(smallest_number_of_three(integer_one, integer_two, integer_three))
