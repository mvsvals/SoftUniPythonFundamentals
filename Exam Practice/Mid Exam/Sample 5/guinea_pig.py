quantity_food = float(input()) * 1000
quantity_hay = float(input()) * 1000
quantity_cover = float(input()) * 1000
guinea_weight = float(input()) * 1000

daily_food_consumption = 300
is_pet_happy = 0

for day in range(1, 31):
    quantity_food -= daily_food_consumption
    if day % 2 == 0:
        quantity_hay -= 0.05 * quantity_food
    if day % 3 == 0:
        quantity_cover -= guinea_weight / 3
    is_pet_happy = (quantity_cover > 0 and quantity_food > 0 and quantity_hay > 0)
    if not is_pet_happy:
        print('Merry must go to the pet store!')
        break

if is_pet_happy:
    print(f'Everything is fine! Puppy is happy! Food: {quantity_food / 1000:.2f}, Hay: {quantity_hay / 1000:.2f}, Cover: {quantity_cover / 1000:.2f}.')