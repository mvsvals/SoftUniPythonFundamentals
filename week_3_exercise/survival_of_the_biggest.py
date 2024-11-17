# Write a program that receives a list of integer numbers (separated by a single space) and a number n.
# The number n represents the count of numbers to remove from the list.
# You should remove the smallest ones, and then, you should print all the numbers that are left in the list, separated by a comma and a space ", ".

input_list = list(map(int, input().split()))
number_input = int(input())

for number in range(number_input):
    input_list.remove(min(input_list))

print(*input_list, sep=", ")
