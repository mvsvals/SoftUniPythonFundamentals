
tour_stops_string = input()

while True:
    input_string = input()
    if input_string == 'Travel':
        break
    command = input_string.split(':')
    if command[0] == 'Add Stop':
        index, string = int(command[1]), command[2]
        if 0 <= index < len(tour_stops_string):
            tour_stops_string = tour_stops_string[:index] + string + tour_stops_string[index:]
    elif command[0] == 'Remove Stop':
        start_index, end_index = int(command[1]), int(command[2])
        if 0 <= start_index <= end_index < len(tour_stops_string):
            tour_stops_string = tour_stops_string[:start_index] + tour_stops_string[end_index+1:]
    elif command[0] == 'Switch':
        old_string, new_string = command[1:]
        if old_string in tour_stops_string:
            tour_stops_string = tour_stops_string.replace(old_string, new_string)
    print(tour_stops_string)

print(f'Ready for world tour! Planned stops: {tour_stops_string}')