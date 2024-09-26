maximum_people_per_wagon = 4

initial_input = input()

if isinstance(initial_input, list):
    people_waiting = initial_input[0]
    state_of_the_lift = initial_input[1]
else:
    people_waiting = int(initial_input)
    state_of_the_lift = input()

wagon_capacity = state_of_the_lift.split(' ')
are_wagons_full = None

for index, wagon in enumerate(wagon_capacity):
    if int(wagon) < maximum_people_per_wagon:
        empty_seats = maximum_people_per_wagon - int(wagon)
        if wagon_capacity.index(wagon) == len(wagon_capacity) - 1:
            if empty_seats > people_waiting:
                wagon_capacity[index] = people_waiting
            else:
                are_wagons_full = True
                wagon_capacity[index] = maximum_people_per_wagon
        else:
            wagon_capacity[index] = maximum_people_per_wagon
        people_waiting -= empty_seats
    else:
        continue

if are_wagons_full:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
else:
    print('The lift has empty spots!')
print(' '.join(map(str, wagon_capacity)))
print(map(str, wagon_capacity))
