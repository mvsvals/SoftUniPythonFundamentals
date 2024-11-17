
# You will be given a string representing the working day events. Each event is separated with '|' (vertical bar): "event1|event2| … eventN"
# Each event contains an event name or an ingredient and a number, separated by a dash ("{event/ingredient}-{number}")
#     • If the event is "rest":
#         ◦ You gain energy (the number in the second part). Note: your energy cannot exceed your initial energy (100). Print: "You gained {gained_energy} energy.".
#         ◦ After that, print your current energy: "Current energy: {current_energy}.".
#     • If the event is "order":
#         ◦ You've earned some coins (the number in the second part).
#         ◦ Each time you get an order, your energy decreases by 30 points.
#             ▪ If you have the energy to complete the order, print: "You earned {earned} coins.".
#             ▪ Otherwise, skip the order and gain 50 energy points. Print: "You had to rest!".
#     • In any other case, you have an ingredient you should buy. The second part of the event contains the coins you should spend.
#         ◦ If you have enough money, you should buy the ingredients and print:
# "You bought {ingredient}."
#         ◦ Otherwise, print "Closed! Cannot afford {ingredient}." and your bakery rush is over.
# If you managed to handle all events throughout the day, print on the following 3 lines:
# "Day completed!"
# "Coins: {coins}"
# "Energy: {energy}"
# Input / Constraints
# You will receive a string representing the working day events, separated with '|' (vertical bar) in the format:
# "event1|event2| … eventN".
# Each event contains an event name or an ingredient and a number, separated by a dash in the format: "{event/ingredient}-{number}"

current_energy, current_coins = 100, 100
max_energy = 100
is_event_failed = False

input_string = input().split('|')

for event in input_string:
    event_list = event.split('-')
    if event_list[0] == 'rest':
        if (int(event_list[1]) + current_energy) >= max_energy:
            difference = max_energy - current_energy
            print(f"You gained {difference} energy.")
            current_energy = 100
            print(f'Current energy: {current_energy}.')
        else:
            print(f'You gained {event_list[1]} energy.')
            current_energy += int(event_list[1])
            print(f'Current energy: {current_energy}.')
    elif event_list[0] == 'order':
        if current_energy >= 30:
            current_energy -= 30
            print(f'You earned {event_list[1]} coins.')
            current_coins += int(event_list[1])
        else:
            print("You had to rest!")
            current_energy += 50
    else:
        if current_coins >= int(event_list[1]):
            print(f"You bought {event_list[0]}.")
            current_coins -= int(event_list[1])
        else:
            print(f"Closed! Cannot afford {event_list[0]}.")
            is_event_failed = True
            break

if not is_event_failed:
    print("Day completed!")
    print(f"Coins: {current_coins}")
    print(f"Energy: {current_energy}")
