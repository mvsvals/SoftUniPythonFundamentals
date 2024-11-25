
cities_dict = {}

while True:
    input_string = input()
    if input_string == 'Sail':
        break
    city, population, gold = input_string.split('||')[0], int(input_string.split('||')[1]), int(input_string.split('||')[2])
    if city in cities_dict:
        cities_dict[city]['population'] += population
        cities_dict[city]['gold'] += gold
    else:
        cities_dict[city] = {'population': population, 'gold': gold}


while True:
    input_string = input()
    if input_string == 'End':
        break
    command = input_string.split('=>')
    if command[0] == 'Plunder':
        city, people, gold = command[1], int(command[2]), int(command[3])
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        cities_dict[city]['population'] -= people
        cities_dict[city]['gold'] -= gold
        if cities_dict[city]['population'] <= 0 or cities_dict[city]['gold'] <= 0:
            print(f'{city} has been wiped off the map!')
            del cities_dict[city]
    elif command[0] == 'Prosper':
        city, gold = command[1], int(command[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities_dict[city]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities_dict[city]['gold']} gold.")

if not cities_dict:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities_dict)} wealthy settlements to go to:")
    for city, city_info in cities_dict.items():
        print(f"{city} -> Population: {city_info['population']} citizens, Gold: {city_info['gold']} kg")