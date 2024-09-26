n_number = int(input())

for k in range(n_number):
    input_number = int(input())
    if input_number % 2 != 0:
        print(f'{input_number} is odd!')
        break
else:
    print('All numbers are even.')
