# You will receive a number representing the number of wagons a train has.
# Create a list (train) with the given length containing only zeros.
# Until you receive the command "End", you will receive some of the following commands:
#
# "add {people}" – you should add the number of people in the last wagon
#
# "insert {index} {people}" - you should add the number of people at the given wagon
#
# "leave {index} {people}" - you should remove the number of people from the wagon. There will be no case in which the people will be more than the count in the wagon.
#
# There will be no case in which the index is invalid!
#
# After you receive the "End" command print the train.


wagons = [0] * int(input())

while True:
    input_command = input().split()
    if 'End' in input_command:
        break
    input_command[1] = int(input_command[1])
    if 'add' in input_command:
        wagons[-1] += input_command[1]
    elif 'insert' in input_command:
        index = int(input_command[1])
        wagons[index] += int(input_command[2])
    elif 'leave' in input_command:
        index = int(input_command[1])
        wagons[index] -= int(input_command[2])

print(wagons)