
current_health = 100
current_bitcoins = 0
is_character_alive = True
dungeon_layout = [dungeon_item for dungeon_item in input().split('|')]

for dungeon_item in dungeon_layout:
    dungeon_command = dungeon_item.split()[0]
    if dungeon_command == 'potion':
        input_healing_amount = int(dungeon_item.split()[1])
        amount_available_to_heal = 100 - current_health
        amount_healed = 0
        if input_healing_amount > amount_available_to_heal:
            current_health = 100
            amount_healed = amount_available_to_heal
        else:
            current_health += input_healing_amount
            amount_healed = input_healing_amount
        print(f"You healed for {amount_healed} hp.")
        print(f"Current health: {current_health} hp.")
    elif dungeon_command == 'chest':
        chest_amount = int(dungeon_item.split()[1])
        print(f"You found {chest_amount} bitcoins.")
        current_bitcoins += chest_amount
    else:
        monster_name = dungeon_command
        monster_attack = int(dungeon_item.split()[1])
        current_health -= monster_attack
        if current_health > 0:
            print(f"You slayed {monster_name}.")
        else:
            print(f"You died! Killed by {monster_name}.")
            print(f"Best room: {dungeon_layout.index(dungeon_item) + 1}")
            is_character_alive = False
            break

if is_character_alive:
    print("You've made it!")
    print(f"Bitcoins: {current_bitcoins}")
    print(f"Health: {current_health}")