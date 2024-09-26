input_rows = int(input())


for row in range(1, input_rows + 1):
    spaced_needed = input_rows - row
    numbers_needed = (row * 2) - 1
    print(" " * spaced_needed, end='')
    for i in range(1, row + 1):
        print(i, end='')
    for k in range(row - 1, 0, -1):
        print(k, end='')
    print()