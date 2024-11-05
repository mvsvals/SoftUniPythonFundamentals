# Write a program that keeps the information about products and their prices.
# Each product has a name, a price, and a quantity:
#     • If the product doesn't exist yet, add it with its starting quantity.
#     • If you receive a product, that already exists, increase its quantity by the input quantity and if its price is different, replace the price as well.
# You will receive products' names, prices, and quantities on new lines.
# Until you receive the command "buy", keep adding items.
# Finally, print all items with their names and the total price of each product.
# Input
#     • Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
#     • The product data is always delimited by a single space.
# Output
#     • Print information about each product in the following format:
# "{product_name} -> {total_price}"
#     • Format the total price to the 2nd digit after the decimal separator.

order_dict = {}

while True:
    input_string = input()
    if input_string == 'buy':
        break
    product_list = input_string.split()
    name, price, quantity = product_list[0], float(product_list[1]), int(product_list[2])
    if name not in order_dict.keys():
        order_dict[name] = {'quantity': 0, 'current_price': 0, 'total_price': 0}
    order_dict[name]['quantity'] += quantity
    order_dict[name]['current_price'] = price

for item in order_dict.keys():
    total_price_calc = order_dict[item]['quantity'] * order_dict[item]['current_price']
    print(f'{item} -> {total_price_calc:.2f}')