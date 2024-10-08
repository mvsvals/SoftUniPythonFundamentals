# You are now to create a program that prints a Josephus permutation, receiving two lines of code:
#     • the list itself - numbers separated by a single space representing the people in the circle
#     • a number k
# People are standing in a circle waiting to be executed. Counting begins from the first one in the circle and proceeds from left to right.
#
# After a specified number of people are skipped, the k person is executed.
# The procedure is repeated with the remaining people, starting with the next person, going in the same direction, and skipping the same number of people until no one remains.
# Print the people by order of executions in the format: "[{executed1},{executed2}, … {executedN}]"

kill_list = input().split()
k_number = int(input())

executed_list = []
current_position = 0

while len(kill_list) > 0:
    current_position = (current_position + k_number - 1) % len(kill_list)
    executed_list.append(kill_list[current_position])
    kill_list.pop(current_position)

print('[' + ','.join(executed_list) + ']')









