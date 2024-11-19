import re

total_calories = 0
total_days = 0

input_string = input()
pattern = r'([#|])([a-zA-Z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'
matches = re.findall(pattern, input_string)

if matches:
    total_calories = sum(int(match[3]) for match in matches)
    total_days = total_calories // 2000

print(f"You have food to last you for: {total_days} days!")

if matches:
    for match in matches:
        print(f"Item: {match[1]}, Best before: {match[2]}, Nutrition: {match[3]}")