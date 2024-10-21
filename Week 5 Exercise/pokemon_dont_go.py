# You will receive a sequence of integers, separated by spaces - the distances to the pokemon. T
# hen you will begin receiving integers, which will correspond to indexes in that sequence.
# When you receive an index, you must remove the element at that index from the sequence (as if you've captured the pokemon).
#     • You must increase the value of all elements in the sequence that are less or equal to the removed element with the value of the removed element.
#     • You must decrease the value of all elements in the sequence that are greater than the removed element with the value of the removed element.
# If the given index is less than 0, remove the first element of the sequence, and copy the last element to its place.
# If the given index is greater than the last index of the sequence, remove the last element from the sequence, and copy the first element to its place.
# The increasing and decreasing elements should also be done in these cases. The element whose value you should use is the removed element.
# The program ends when the sequence has no elements (there are no pokemon left for Ely to catch).
# Input
#     • On the first line of input, you will receive a sequence of integers, separated by spaces.
#     • On the next several lines, you will receive integers - the indexes.
# Output
#     • When the program ends, you must print the summed value of all removed elements.
# Constraints
#     • The input data will consist only of valid integers in the range [-2.147.483.648…2.147.483.647].

distance_list = [int(distance) for distance in input().split()]
removed_elements = []
removed_index = 0

while len(distance_list) > 0:
    input_index = int(input())

    if input_index < 0:
        removed_elements.append(distance_list[0])
        distance_list.pop(0)
        distance_list.insert(0, distance_list[-1])
    elif input_index > len(distance_list) - 1:
        removed_elements.append(distance_list[-1])
        distance_list.pop(-1)
        distance_list.append(distance_list[0])
    else:
        removed_elements.append(distance_list[input_index])
        distance_list.pop(input_index)
    distance_list = list(
        map(lambda x: x + removed_elements[removed_index] if x <= removed_elements[removed_index] else x - removed_elements[removed_index], distance_list))
    removed_index += 1

print(sum(removed_elements))
