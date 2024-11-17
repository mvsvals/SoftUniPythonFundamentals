# Write a program that calculates the total cost of bought furniture.
# You will be given information about each purchase on separate lines until you receive the command "Purchase".
# Valid information should be in the format: ">>{furniture_name}<<{price}!{quantity}".
# The price could be a floating-point or integer number. You should store the names of the furniture and the total price.
# In the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:
# "Bought furniture:
# {1st name}
# {2nd name}
# …
# {N name}
# Total money spend: {total_cost}"
import re

total_value = 0
furniture_list = []

while True:
    input_string = input()
    if input_string == 'Purchase':
        break
    pattern = r'>>([A-Za-z0-9\s\-]+)<<(\d+(\.\d+)?)!([1-9][0-9]*)'
    matches = re.findall(pattern, input_string)
    if matches:
        furniture_name = matches[0][0]
        price = float(matches[0][1])
        quantity = int(matches[0][3])
        total_value += price * quantity
        furniture_list.append(furniture_name)

# Printing results
print('Bought furniture:')
for furniture in furniture_list:
    print(furniture)
print(f'Total money spend: {total_value:.2f}')
