total_price = 0
is_special_customer = None

while True:
    input_price_string = input()
    if input_price_string == 'special':
        is_special_customer = True
        break
    elif input_price_string == 'regular':
        break
    if float(input_price_string) < 0:
        print('Invalid price!')
        continue
    else:
        total_price += float(input_price_string)

if total_price == 0:
    print('Invalid order!')
else:
    taxes = total_price * 0.2
    print('Congratulations you\'ve just bought a new computer!')
    print(f'Price without taxes: {total_price:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    if is_special_customer:
        print(f'Total price: {(total_price + taxes) * 0.90:.2f}$')
    else:
        print(f'Total price: {total_price + taxes:.2f}$')
