# Write a program that receives a single string containing positive and negative numbers separated by a single space.
# Print a list containing the opposite of each number.


input_string = input()
numbers_list = input_string.split(' ')
opposite_list = []

for number in numbers_list:
       opposite_list.append(int(number) * -1)

print(opposite_list)
