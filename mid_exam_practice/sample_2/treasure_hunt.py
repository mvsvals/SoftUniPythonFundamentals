
# The following lines represent commands until "Yohoho!" which ends the treasure hunt:
#     • "Loot {item1} {item2}…{itemn}":
#         ◦ Pick up treasure loot along the way. Insert the items at the beginning of the chest.
#         ◦ If an item is already contained, don't insert it.
#     • "Drop {index}":
#         ◦ Remove the loot at the given position and add it at the end of the treasure chest.
#         ◦ If the index is invalid, skip the command.
#     • "Steal {count}":
#         ◦ Someone steals the last count of loot items. If there are fewer items than the given count, remove as many as there are.
#         ◦ Print the stolen items separated by ", ":
# "{item1}, {item2}, {item3} … {itemn}"
# In the end, output the average treasure gain, which is the sum of all treasure items' length divided by the count of all items inside the chest formatted to the second decimal point:
# "Average treasure gain: {averageGain} pirate credits."
# If the chest is empty, print the following message:
# "Failed treasure hunt."


def loot(items):
    items_to_add = [item for item in items if item not in initial_treasure_chest]
    if len(items_to_add) > 0:
        for item in items_to_add:
            initial_treasure_chest.insert(0, item)

def drop(index):
    if index in range(0, len(initial_treasure_chest) - 1):
        string_to_append = initial_treasure_chest[index]
        initial_treasure_chest.pop(index)
        initial_treasure_chest.append(string_to_append)

def steal(count):
    global initial_treasure_chest
    if len(initial_treasure_chest) > count:
        stolen_items = initial_treasure_chest[-1:-(count + 1):-1]
        for element in range(count):
            initial_treasure_chest.pop(-1)
    else:
        stolen_items = initial_treasure_chest[::-1]
        initial_treasure_chest = []
    print(', '.join(stolen_items[::-1]))


initial_treasure_chest = input().split('|')

while True:
    input_command = input().split()
    action = input_command[0]
    if action == 'Yohoho!':
        break
    elif action == 'Loot':
        items_for_function = input_command[1:]
        loot(items_for_function)
    elif action == 'Drop':
        index_for_function = int(input_command[1])
        drop(index_for_function)
    elif action == 'Steal':
        count_for_function = int(input_command[1])
        steal(count_for_function)

if not initial_treasure_chest:
    print('Failed treasure hunt.')
else:
    average_treasure_gain = sum(len(element) for element in initial_treasure_chest) / len(initial_treasure_chest)
    print(f'Average treasure gain: {average_treasure_gain:.2f} pirate credits.')




