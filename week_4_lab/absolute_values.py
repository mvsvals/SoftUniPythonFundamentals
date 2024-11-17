# Write a program that receives a sequence of numbers,
# separated by a single space, and prints their absolute value as a list. Use abs().

input_numbers = [abs(float(number)) for number in input().split()]
print(input_numbers)