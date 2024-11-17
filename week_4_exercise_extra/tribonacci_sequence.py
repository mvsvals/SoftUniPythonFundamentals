# In the Tribonacci sequence, every number is formed by the sum of the previous 3.
# Write a function that prints numbers from the Tribonacci sequence on one line separated by a single space, starting from 1.
# You will receive a positive integer number as input.


input_integer = int(input())

def tribonacci_sequence(total_numbers: int) -> str:
    numbers_list = [1]
    for number in range(input_integer - 1):
        numbers_list.append(sum(numbers_list[-1:-4:-1]))
    print(*numbers_list)

tribonacci_sequence(input_integer)
