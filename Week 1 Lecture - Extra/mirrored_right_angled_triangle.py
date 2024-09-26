input_rows = int(input())

for row in range(1, input_rows + 1):
    spaces_needed = (input_rows - row)
    print(" " * spaces_needed + "*" * row)


