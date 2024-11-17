# Create a function that receives three parameters, calculates a result depending on the given operator, and returns it.
# Print the result of the function.
# The input comes as three parameters – an operator as a string and two integer numbers. The operator can be one of the following:  "multiply", "divide", "add", and "subtract".

def calculate(operator: str, num1: int, num2: int):
    result = 0
    if operator == 'multiply':
        result = num1 * num2
    elif operator == 'divide':
        result = num1 / num2
    elif operator == 'add':
        result = num1 + num2
    elif operator == 'subtract':
        result = num1 - num2
    return result

operator_input = input()
number_one_input = int(input())
number_two_input = int(input())

result = calculate(operator_input, number_one_input, number_two_input)
print(f'{result:.0f}')

