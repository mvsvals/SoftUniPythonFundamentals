food_inventory = {}
food_sales = 0


while True:
    input_string = input()
    if input_string == "Complete":
        break
    command, quantity, food = input_string.split()
    if command == 'Receive' and int(quantity) > 0:
        if not food in food_inventory:
            food_inventory[food] = int(quantity)
        else:
            food_inventory[food] += int(quantity)

    elif command == 'Sell':
        if not food in food_inventory:
            print(f'You do not have any {food}.')
        else:
            if food_inventory[food] >= int(quantity):
                print(f"You sold {quantity} {food}.")
                food_inventory[food] -= int(quantity)
                if food_inventory[food] == 0:
                    food_inventory.pop(food)
                food_sales += int(quantity)
            else:
                print(f"There aren't enough {food}. You sold the last {food_inventory[food]} of them.")
                food_sales += food_inventory[food]
                food_inventory.pop(food)

for x in food_inventory.items():
    print(f'{x[0]}: {x[1]}')

print(f'All sold: {food_sales} goods')