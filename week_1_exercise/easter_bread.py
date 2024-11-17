# Ingredients needed per one loaf
egg_packs = 1
flour_kg = 1
milk_ml = 0.250

# Inputs
budget = float(input())
flour_price_per_kg = float(input())
egg_price_per_pack = 0.75 * flour_price_per_kg
milk_price_per_liter = 1.25 * flour_price_per_kg

# Loaf price
loaf_price = egg_packs * egg_price_per_pack + flour_kg * flour_price_per_kg + milk_price_per_liter * milk_ml

colored_eggs_count = 0
total_loaves_made = int(budget // loaf_price)
funds_remainder = budget % loaf_price

for i in range(1, total_loaves_made + 1):
    colored_eggs_count += 3
    if i % 3 == 0:
        colored_eggs_count -= i - 2

print(f'You made {total_loaves_made} loaves of Easter bread! Now you have {colored_eggs_count} eggs and {funds_remainder:.2f}BGN left.')


