#  The possible items are:
#     • "Shadowmourne" - requires 250 Shards
#     • "Valanyr" - requires 250 Fragments
#     • "Dragonwrath" - requires 250 Motes
# "Shards", "Fragments", and "Motes" are the key materials 	(case-insensitive), and everything else is junk.
# You will be given lines of input in the format:
# "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
# Keep track of the key materials - the first one that reaches 250, wins the race. At that point, you have to print that the corresponding legendary item is obtained.
# In the end, print the remaining shards, fragments, and motes in the format:
# "shards: {number_of_shards}
# fragments: {number_of_fragments}
# motes: {number_of_motes}"
# Finally, print the collected junk items in the order of appearance.

# Input
#     • Each line comes in the following format: "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"

# Output
#     • On the first line, print the obtained item in the format: "{Legendary item} obtained!"
#     • On the next three lines, print the remaining key materials
#     • On the several final lines, print the junk items
#     • All materials should be printed in the format: "{material}: {quantity}"
#     • The output should be lowercase, except for the first letter of the legendary

item_dict = {'valuable': {
                'shards': {
                    'amount': 0,
                    'reward': 'Shadowmourne'
                    },
                'fragments': {
                    'amount': 0,
                    'reward': 'Valanyr'
                    },
                'motes': {
                    'amount': 0,
                    'reward': 'Dragonwrath'
                    },
                },
             'junk': {}
             }

is_item_obtained = False

while True:
    input_string = input().lower().split()
    for i in range(0, len(input_string), 2):
        key = input_string[i + 1]
        value = int(input_string[i])
        if key not in item_dict['valuable'].keys():
            if key in item_dict['junk'].keys():
                item_dict['junk'][key] += value
            else:
                item_dict['junk'][key] = value
        else:
            item_dict['valuable'][key]['amount'] += value
            if item_dict['valuable'][key]['amount'] >= 250:
                print(f"{item_dict['valuable'][key]['reward']} obtained!")
                item_dict['valuable'][key]['amount'] -= 250
                is_item_obtained = True
                break
    if is_item_obtained:
        break

for key, value in item_dict['valuable'].items():
    print(f"{key}: {item_dict['valuable'][key]['amount']}")

for key, value in item_dict['junk'].items():
    print(f'{key}: {value}')


