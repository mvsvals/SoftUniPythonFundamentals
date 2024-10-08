# You will receive three integer numbers.
# Write a program that finds if their multiplication (the result) is negative, positive, or zero.
# Try to do this WITHOUT multiplying the 3 numbers.

input_integers = [int(input()), int(input()), int(input())]

def multiplication_analyze(integers: list) -> str:
    if 0 in integers:
        return 'zero'
    negative_numbers = [num for num in input_integers if num < 0]
    if len(negative_numbers) == 1 or len(negative_numbers) == 3:
        return 'negative'
    else:
        return 'positive'

print(multiplication_analyze(input_integers))