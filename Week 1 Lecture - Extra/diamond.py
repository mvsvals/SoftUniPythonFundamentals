#  a Python script that displays a diamond pattern based on the number of rows (height) specified by the user.
#  For instance, if the user enters 5, the output should resemble the following:

#   *
#  ***
# *****
#  ***
#   *

input_rows = int(input())

for row in range(1, input_rows + 1, 2):
    spacing = (input_rows - row) // 2
    print(" " * spacing + "*" * row)
for row in range(input_rows - 2, 0, -2):
    spacing = (input_rows - row) // 2
    print(" " * spacing + "*" * row)
