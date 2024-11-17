import re

total_money = 0

while True:
    input_string = input()
    if input_string == 'end of shift':
        break
    pattern = r'%([A-Z][a-z]+)%[^|$%.0-9]*<(\w+)>[^|$%.0-9]*\|(\d+)\|[^|$%.0-9]*([0-9]+\.?\d*)\$'
    match = re.findall(pattern, input_string)
    if match:
        total_order_cost = int(match[0][2]) * float(match[0][3])
        print(f"{match[0][0]}: {match[0][1]} - {total_order_cost:.2f}")
        total_money += total_order_cost

print(f"Total income: {total_money:.2f}")