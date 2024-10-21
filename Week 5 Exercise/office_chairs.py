# On the first line, you will be given an integer n representing the number of rooms in the business center.
# On the following n lines for each room, you will receive information about the chairs in the room and the number of visitors.
# Each chair will be presented with the char "X". Next, there will be a single space and the number of visitors at the end.
# For example: "XXXXX 4" (5 chairs and 4 visitors).
# Keep track of the free chairs:
#     • If there are not enough chairs in a specific room, print the following message: "{needed_chairs_in_room} more chairs needed in room {number_of_room}". The rooms start from 1.
#     • Otherwise, print: "Game On, {total_free_chairs} free chairs left".


number_of_rooms = int(input())
free_chairs = 0
are_there_enough_chairs = True

for room in range(1, number_of_rooms + 1):
    input_command = input().split()
    chairs = len(input_command[0])
    visitors = int(input_command[1])
    if visitors > chairs:
        print(f'{visitors - chairs} more chairs needed in room {room}')
        are_there_enough_chairs = False
    free_chairs += chairs - visitors

if are_there_enough_chairs:
    print(f'Game On, {free_chairs} free chairs left')
