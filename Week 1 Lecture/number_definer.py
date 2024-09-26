input_number = float(input())
if input_number == 0:
    print('zero')
elif input_number > 0:
    if abs(input_number) < 1:
        print('small positive')
    elif input_number > 1_000_000:
        print('large positive')
    else:
        print('positive')
else:
    if abs(input_number) < 1:
        print('small negative')
    elif abs(input_number) > 1_000_000:
        print('large negative')
    else:
        print('negative')
