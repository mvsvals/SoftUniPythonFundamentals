shopping_list = input().split("!")

while True:
    input_command = input()
    if input_command == 'Go Shopping!':
        break
    input_command = input_command.split()
    if input_command[0] == "Urgent":
        item = input_command[1]
        if item not in shopping_list:
            shopping_list.insert(0, item)
    elif input_command[0] == "Unnecessary":
        item = input_command[1]
        if item in shopping_list:
            shopping_list.remove(item)
    elif input_command[0] == "Correct":
        old_item, new_item = input_command[1], input_command[2]
        if old_item in shopping_list:
            old_item_index = shopping_list.index(old_item)
            shopping_list[old_item_index] = new_item
    elif input_command[0] == 'Rearrange':
        item = input_command[1]
        if item in shopping_list:
            shopping_list.append(item)
            shopping_list.remove(item)

print(*shopping_list, sep=", ")