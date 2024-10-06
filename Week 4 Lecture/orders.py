# Write a function that calculates the total price of an order and returns it.
# The function should receive one of the following products: "coffee", "coke", "water", or "snacks", and a quantity of the product.
# The prices for a single piece of each product are:
#     • coffee - 1.50
#     • water - 1.00
#     • coke - 1.40
#     • snacks - 2.00
#
# Print the result formatted to the second decimal place.


def calculate_order_total(item: str, quantity: int):
    order_total = 0
    if item == 'coffee':
        order_total = 1.50 * quantity
    elif item == 'water':
        order_total = 1.00 * quantity
    elif item == 'coke':
        order_total = 1.40 * quantity
    elif item == 'snacks':
        order_total = 2.00 * quantity
    return order_total


input_item = input()
item_quantity = int(input())

print(f'{calculate_order_total(input_item, item_quantity):.2f}')
