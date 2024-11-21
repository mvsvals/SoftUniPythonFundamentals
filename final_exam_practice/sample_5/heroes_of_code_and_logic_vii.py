
max_hp = 100
max_mp = 200

total_heroes = int(input())
heroes_dict = {}

for x in range(total_heroes):
    hero_name, hp, mp = input().split()
    heroes_dict[hero_name] = [int(hp), int(mp)]

while True:
    input_command = input().split(' - ')
    if input_command[0] == 'End':
        break
    if input_command[0] == 'CastSpell':
        hero_name, mp_needed, spell_name = input_command[1], int(input_command[2]), input_command[3]
        if heroes_dict[hero_name][1] >= mp_needed:
            heroes_dict[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif input_command[0] == 'TakeDamage':
        hero_name, damage, attacker = input_command[1], int(input_command[2]), input_command[3]
        heroes_dict[hero_name][0] -= damage
        if heroes_dict[hero_name][0] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero_name][0]} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes_dict[hero_name]
    elif input_command[0] == 'Recharge':
        hero_name, amount = input_command[1], int(input_command[2])
        if heroes_dict[hero_name][1] + amount > max_mp:
            amount = max_mp - heroes_dict[hero_name][1]
            heroes_dict[hero_name][1] = max_mp
        else:
            heroes_dict[hero_name][1] += amount
        print(f"{hero_name} recharged for {amount} MP!")

    elif input_command[0] == 'Heal':
        hero_name, amount = input_command[1], int(input_command[2])
        if heroes_dict[hero_name][0] + amount > max_hp:
            amount = max_hp - heroes_dict[hero_name][0]
            heroes_dict[hero_name][0] = max_hp
        else:
            heroes_dict[hero_name][0] += amount
        print(f"{hero_name} healed for {amount} HP!")

for hero, stats in heroes_dict.items():
    print(f'{hero}\n  HP: {stats[0]}\n  MP: {stats[1]}')