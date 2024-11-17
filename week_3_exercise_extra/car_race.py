# Write a program that announces the winner of a car race.
# You will receive a sequence of numbers.
# Each number represents the time the car needs to pass through that step (the index).
# There will be two cars. The first one starts from the left side, and the other one starts from the right side.
# The middle index of the sequence is the finish line.
# Calculate the total time each racer needs to reach the finish line and print the winner with his total time (the racer with less time).
# If you have a zero in the list, you should reduce the racer's time that reached it by 20% (from his current time).
# The number of elements in the sequence will always be odd.
# Print the result in the following format "The winner is {left/right} with total time: {total_time}".
# The time should be formatted to the first decimal point.


input_numbers = list(map(int, input().split()))

winner = 0
middle_index = len(input_numbers) // 2 + 1
total_time_left, total_time_right, best_time = 0, 0, 0

for left_time in input_numbers[:middle_index - 1]:
    if left_time == 0:
        total_time_left *= 0.80
    else:
        total_time_left += left_time

for right_time in input_numbers[:middle_index - 1:-1]:
    if right_time == 0:
        total_time_right *= 0.80
    else:
        total_time_right += right_time


if total_time_right > total_time_left:
    winner = 'left'
    best_time = total_time_left
else:
    winner = 'right'
    best_time = total_time_right

print(f"The winner is {winner} with total time: {best_time:.1f}")











