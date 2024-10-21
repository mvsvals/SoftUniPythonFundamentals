# You will receive a journal with some collecting items, separated with a comma and a space (", ").
# After that, until receiving "Craft!" you will be receiving different commands split by " - ":
#     • "Collect - {item}" - you should add the given item to your inventory. If the item already exists, you should skip this line.
#     • "Drop - {item}" - you should remove the item from your inventory if it exists.
#     • "Combine Items - {old_item}:{new_item}" - you should check if the old item exists. If so, add the new item after the old one. Otherwise, ignore the command.
#     • "Renew – {item}" – if the given item exists, you should change its position and put it last in your inventory.
# Output
# After receiving "Craft!" print the items in your inventory, separated by ", ".
# Examples


journal_of_items = input().split(", ")

while True:
    input_string = input()
    if input_string == 'Craft!':
        break
    input_string = input_string.split(' - ')
    command, item = input_string[0], input_string[1]
    if command == 'Collect' and item not in journal_of_items:
        journal_of_items.append(item)
    elif command == 'Drop' and item in journal_of_items:
        journal_of_items.remove(item)
    elif command == 'Combine Items':
        if item.split(':')[0] in journal_of_items:
            items = input_string[1].split(':')
            item1 = items[0]
            item2 = items[1]
            old_item_index = journal_of_items.index(item.split(':')[0])
            journal_of_items.insert(old_item_index + 1, item2)
    elif command == 'Renew' and item in journal_of_items:
        item_index = journal_of_items.index(item)
        journal_of_items.pop(item_index)
        journal_of_items.append(item)

print(*journal_of_items, sep=', ')