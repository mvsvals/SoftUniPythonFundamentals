# Craft a Python program that produces a square pattern with a hollow center. The program should take the size of the square as input from the user. Here's an example output for a user input of 5:

# *****
# *   *
# *   *
# *   *
# *****

input_size_of_square = int(input())

print("*" * input_size_of_square)

for row in range(input_size_of_square - 2):
    for col in range(1, input_size_of_square + 1):
        if col == 1:
            print("*", end='')
        elif 1 < col < input_size_of_square:
            print(' ', end='')
        else:
            print("*")

print("*" * input_size_of_square)