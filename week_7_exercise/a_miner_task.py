# You will be given a sequence of strings, each on a new line until you receive the "stop" command.
# Every odd line on the console represents a resource (e.g., Gold, Silver, Copper, and so on) and every even - quantity.
# Your task is to collect the resources and print them each on a new line.
# Print the resources and their quantities in the following format:
# "{resource} -> {quantity}"
# The quantities will be in the range [1 … 2 000 000 000].

resource_dict = {}

while True:
    input_string = input()
    if input_string == 'stop':
        break
    quantity = int(input())
    if input_string not in resource_dict.keys():
        resource_dict[input_string] = quantity
    else:
        resource_dict[input_string] += quantity

for key, value in resource_dict.items():
    print(f'{key} -> {value}')
