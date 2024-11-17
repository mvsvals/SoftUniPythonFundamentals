# Write a Python script that prints a square pattern where stars and dashes alternate in each row. The size of the square should be provided by the user. Here's an example for user input of 5:

# *-*-*
# -*-*-
# *-*-*
# -*-*-
# *-*-*

input_square_size = int(input())

for row in range(1, input_square_size + 1):
    if row % 2 != 0:
        print("*-" * (input_square_size // 2) + "*" * (input_square_size % 2))
    else:
        print("-*" * (input_square_size // 2) + "-" * (input_square_size % 2))



