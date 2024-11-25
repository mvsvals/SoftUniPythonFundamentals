
import re

total_calories = 0
total_days_with_food = 0

food_input_string = input()
pattern = r'([#|])([a-zA-Z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'

matches = re.findall(pattern, food_input_string)

if matches:
    total_calories = sum(int(match[3]) for match in matches)
    total_days_with_food = total_calories // 2000

print(f"You have food to last you for: {total_days_with_food} days!")

for food in matches:
    print(f"Item: {food[1]}, Best before: {food[2]}, Nutrition: {food[3]}")