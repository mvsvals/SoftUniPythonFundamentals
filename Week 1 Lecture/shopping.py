budget = int(input())

while True:
    price_of_product = input()
    if price_of_product == 'End':
        print('You bought everything needed.')
        break
    price_of_product = int(price_of_product)
    if price_of_product > budget:
        print('You went in overdraft!')
        break
    else:
        budget -= price_of_product