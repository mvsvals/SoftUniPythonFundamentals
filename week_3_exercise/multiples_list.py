# Write a program that receives two numbers (factor and count).
# It should create a list with a length of the given count that contains only integer numbers, which are multiples of the given factor.
# The numbers should be only positive, and they should be arranged in ascending order, starting from the value of the factor.

input_factor = int(input())
input_count = int(input())

multiples_list = []

for num in range(1, input_count + 1):
    multiples_list.append(num * input_factor)

print(multiples_list)