input_number = int(input())

for row in range(1, input_number + 1):
    print("*" * row)
for row2 in range(input_number - 1, 0, -1):
    print("*" * row2)