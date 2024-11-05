# Your first task at your new job is to create a table of the stock in a bakery, and you really don't want to fail on your first day at work.
# You will receive a single line containing some food (keys) and quantities (values).
# They will be separated by a single space (the first element is the key, the second – is the value, and so on).
# Create a dictionary with all the keys and values and print it on the console.

input_data = input().split()

stock_table = {}

for i in range(0, len(input_data), 2):
    key = input_data[i]
    value = input_data[i+1]
    stock_table[key] = int(value)

print(stock_table)