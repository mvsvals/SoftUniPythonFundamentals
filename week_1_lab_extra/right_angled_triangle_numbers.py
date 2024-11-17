# Write a Python program that prints a right-angled triangle using numbers. The user will provide the number of rows. For example, if the user inputs 5, the output should look like this:

# 1
# 12
# 123
# 1234
# 12345



input_rows = int(input())

for row in range(1, input_rows + 1):
    for number in range(1, row + 1):
        print(number, end='')
    print()


