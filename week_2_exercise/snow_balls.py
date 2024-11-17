import sys

number_of_snow_balls = int(input())
best_snowball = -sys.maxsize
best_snowball_weight = 0
best_snowball_time = 0
best_snowball_quality = 0

for i in range(number_of_snow_balls):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_weight / snowball_time) ** snowball_quality
    if best_snowball <= snowball_value:
        best_snowball = int(snowball_value)
        best_snowball_time = snowball_time
        best_snowball_weight = snowball_weight
        best_snowball_quality = snowball_quality

print(f"{best_snowball_weight} : {best_snowball_time} = {best_snowball} ({best_snowball_quality})")