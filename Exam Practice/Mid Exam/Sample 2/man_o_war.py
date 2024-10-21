
#     • "Fire {index} {damage}" - the pirate ship attacks the warship with the given damage at that section.
#     Check if the index is valid and if not, skip the command.
#     If the section breaks (health <= 0) the warship sinks, print the following and stop the program: "You won! The enemy ship has sunken."

#     • "Defend {startIndex} {endIndex} {damage}" - the warship attacks the pirate ship with the given damage at that range (indexes are inclusive). Check if both indexes are valid and if not, skip the command. If the section breaks (health <= 0) the pirate ship sinks, print the following and stop the program:
# "You lost! The pirate ship has sunken."

#     • "Repair {index} {health}" - the crew repairs a section of the pirate ship with the given health.
#     Check if the index is valid and if not, skip the command.
#     The health of the section cannot exceed the maximum health capacity.

#     • "Status" - prints the count of all sections of the pirate ship that need repair soon, which are all sections that are lower than 20% of the maximum health capacity.
#     Print the following: "{count} sections need repair."

# In the end, if a stalemate occurs, print the status of both ships, which is the sum of their individual sections, in the following format:
# "Pirate ship status: {pirateShipSum}
# Warship status: {warshipSum}"



status_of_pirate_ship = [int(status) for status in input().split('>')]
status_of_warship = [int(status) for status in input().split('>')]
ship_maximum_health = int(input())
stalemate = True

while True:
    input_command = input().split()
    if input_command[0] == 'Retire':
        break
    elif input_command[0] == 'Fire':
        index, damage = int(input_command[1]), int(input_command[2])
        if 0 <= index <= (len(status_of_warship) - 1):
            status_of_warship[index] -= damage
            if status_of_warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                stalemate = False
                break
    elif input_command[0] == 'Defend':
        startindex, endindex, damage = int(input_command[1]), int(input_command[2]), int(input_command[3])
        if 0 <= startindex <= (len(status_of_pirate_ship) - 1) and 0 <= endindex <= (len(status_of_pirate_ship) - 1):
            for shot in range(startindex, endindex + 1):
                status_of_pirate_ship[shot] -= damage
                if status_of_pirate_ship[shot] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    stalemate = False
                    break
    elif input_command[0] == 'Repair':
        index, health = int(input_command[1]), int(input_command[2])
        if 0 <= index <= (len(status_of_pirate_ship) - 1):
            status_of_pirate_ship[index] += health
            if status_of_pirate_ship[index] > ship_maximum_health:
                status_of_pirate_ship[index] = ship_maximum_health

    elif input_command[0] == 'Status':
        sections_that_need_repair = [section for section in status_of_pirate_ship if section < (0.20 * ship_maximum_health)]
        print(f"{len(sections_that_need_repair)} sections need repair.")
        pass

if stalemate:
    print(f"Pirate ship status: {sum(status_of_pirate_ship)}")
    print(f"Warship status: {sum(status_of_warship)}")