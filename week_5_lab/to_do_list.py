# You will be receiving to-do notes until you get the command "End". The notes will be in the format: "{importance}-{note}".
#
# Return a list containing all to-do notes sorted by importance in ascending order.
#
# The importance value will always be an integer between 1 and 10 (inclusive).
#
# Hint
#
# Use the pop() and insert() methods.

sorted_list = [0] * 10

while True:
    input_note = input()
    if input_note == 'End':
        break
    input_note = input_note.split('-')
    sorted_list.pop(int(input_note[0]) - 1)
    sorted_list.insert(int(input_note[0]) - 1, input_note[1])

print([item for item in sorted_list if item != 0])


