
import math

budget = float(input())
students = int(input())
price_flour_package = float(input())
price_single_egg = float(input())
price_single_apron = float(input())
free_flour = students // 5


flour_needed = (students - free_flour) * price_flour_package
eggs_needed = students * 10 * price_single_egg
aprons_needed = (math.ceil(students * 1.2)) * price_single_apron

total_funds_needed = flour_needed + eggs_needed + aprons_needed

if total_funds_needed > budget:
    print(f"{abs(total_funds_needed - budget):.2f}$ more needed.")
else:
    print(f"Items purchased for {total_funds_needed:.2f}$.")
