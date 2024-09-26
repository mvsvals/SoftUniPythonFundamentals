# Create a Python script that prints a pyramid pattern based on the user-input number of rows. For example, if the user inputs 4, the output should be:

#    *
#   ***
#  *****
# *******

input_rows = int(input())

for row in range(1, input_rows + 1):
    spacing = input_rows - row
    number_of_stars = (row * 2) - 1
    print(" " * spacing, "*" * number_of_stars)
