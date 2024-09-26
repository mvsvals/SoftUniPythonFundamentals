# Prices
ornament_set_price = 2
ornament_set_points = 5

tree_skirt_price = 5
tree_skirt_points = 3

tree_garland_price = 3
tree_garland_points = 10

tree_lights_price = 15
tree_lights_points = 17

total_cost = 0
total_spirit = 0

decorations_quantity_per_trip = int(input())
days = int(input())

for day in range(1, days + 1):
    if day % 11 == 0:
        decorations_quantity_per_trip += 2
    if day % 2 == 0:
        total_cost += ornament_set_price * decorations_quantity_per_trip
        total_spirit += ornament_set_points
    if day % 3 == 0:
        total_cost += tree_skirt_price * decorations_quantity_per_trip + tree_garland_price * decorations_quantity_per_trip
        total_spirit += tree_skirt_points + tree_garland_points
    if day % 5 == 0:
        total_cost += tree_lights_price * decorations_quantity_per_trip
        total_spirit += tree_lights_points
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt_price + tree_garland_price + tree_lights_price
    if day == days and day % 10 == 0:
        total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")


