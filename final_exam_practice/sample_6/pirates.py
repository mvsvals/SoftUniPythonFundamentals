
cities_to_attack = {}

while True:
    input_string = input()
    if input_string == 'Sail':
        break
    command = input_string.split('||')
    city, population, gold = command[0], int(command[1]), int(command[2])
    if city not in cities_to_attack:
        cities_to_attack[city] = [population, gold]
    else:
        cities_to_attack[city][0] += population
        cities_to_attack[city][1] += gold

while True:
    input_string = input()
    if input_string == 'End':
        break
    command = input_string.split('=>')
    if command[0] == 'Plunder':
        city, people, gold = command[1], int(command[2]), int(command[3])
        cities_to_attack[city][0] -= people
        cities_to_attack[city][1] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities_to_attack[city][0] <= 0 or cities_to_attack[city][1] <= 0:
            print(f"{city} has been wiped off the map!")
            del cities_to_attack[city]
    elif command[0] == 'Prosper':
        city, gold = command[1], int(command[2])
        if gold > 0:
            cities_to_attack[city][1] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities_to_attack[city][1]} gold.")
        else:
            print("Gold added cannot be a negative number!")

if not cities_to_attack:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities_to_attack)} wealthy settlements to go to:")
    for city, info in cities_to_attack.items():
        print(f'{city} -> Population: {info[0]} citizens, Gold: {info[1]} kg')