# You will be receiving key-value pairs on separate lines separated by ": " until you receive the command "statistics".
# Sometimes you may receive a product more than once. In that case, you have to add the new quantity to the existing one.
# When you receive the "statistics" command, print the following:
# "Products in stock:
# - {product1}: {quantity1}
# - {product2}: {quantity2}
# …
# - {productN}: {quantityN}
# Total Products: {count_all_products}
# Total Quantity: {sum_all_quantities}"

sample_dict = {}

while True:
    input_string = input()
    if input_string == 'statistics':
        break
    input_string = input_string.split(': ')
    key = input_string[0]
    value = int(input_string[1])
    if key in sample_dict:
        sample_dict[key] += value
    else:
        sample_dict[key] = value

print("Products in stock:")
for element in sample_dict:
    print(f'- {element}: {sample_dict[element]}')

print(f'Total Products: {len(sample_dict.keys())}')
print(f'Total Quantity: {sum(sample_dict.values())}')