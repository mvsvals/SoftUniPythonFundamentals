
dragon_db = {}

number_of_dragons = int(input())


def create_dragon(data_info: list):
    d_type: str = data_info[0]
    d_name: str = data_info[1]
    d_damage: int = data_info[2]
    d_health: int = data_info[3]
    d_armor: int = data_info[4]
    if d_type not in dragon_db:
        dragon_db[d_type] = {}
    if d_damage == 'null':
        d_damage = 45
    if d_health == 'null':
        d_health = 250
    if d_armor == 'null':
        d_armor = 10
    dragon_db[d_type][d_name] = (int(d_damage), int(d_health), int(d_armor))

for i in range(number_of_dragons):
    create_dragon(input().split())

for dragon_type in dragon_db:
    type_average_stats = [0, 0, 0]
    sorted_dragons_list = dict(sorted(dragon_db[dragon_type].items()))

    for dragon in dragon_db[dragon_type]:
        type_average_stats[0] += dragon_db[dragon_type][dragon][0]
        type_average_stats[1] += dragon_db[dragon_type][dragon][1]
        type_average_stats[2] += dragon_db[dragon_type][dragon][2]

    type_average_stats = list(map(lambda x: x / len(dragon_db[dragon_type]), type_average_stats))
    print(f"{dragon_type}::({type_average_stats[0]:.2f}/{type_average_stats[1]:.2f}/{type_average_stats[2]:.2f})")

    for dragon in sorted_dragons_list:
        print(f"-{dragon} -> damage: {dragon_db[dragon_type][dragon][0]}, health: {dragon_db[dragon_type][dragon][1]},"
              f" armor: {dragon_db[dragon_type][dragon][2]}")

