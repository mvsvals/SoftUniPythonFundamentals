# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a list of only the even numbers. Use filter().

input_numbers = [int(num) for num in input().split()]
print(list(filter(lambda num: num % 2 == 0, input_numbers)))

