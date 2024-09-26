# Develop a Python script that prints an inverted pyramid pattern based on the number of rows provided by the user. For instance, if the user inputs 5, the output should be:

# *********
#  *******
#   *****
#    ***
#     *


input_rows = int(input())

for row in range(input_rows, 0, -1):
    spaces_needed = input_rows - row
    stars_needed = (row * 2) - 1
    print(" " * spaces_needed + "*" * stars_needed)