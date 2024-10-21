# On the first input line, you will receive the initial schedule of lessons and exercises that will be part of the next course, separated by a comma and a space ", ".
# Until you receive the "course start" command, you will be given some commands to modify the course schedule.
# The possible commands are:
#     • "Add:{lessonTitle}" - add the lesson to the end of the schedule if it does not exist.
#     • "Insert:{lessonTitle}:{index}" - insert the lesson to the given index, if it does not exist.
#     • "Remove:{lessonTitle}" - remove the lesson, if it exists.
#     • "Swap:{lessonTitle}:{lessonTitle}" - swap the position of the two lessons if they exist.
#     • "Exercise:{lessonTitle}" - add Exercise in the schedule right after the lesson index, if the lesson exists and there is no exercise already, in the following format "{lessonTitle}-Exercise". If the lesson doesn't exist, add the lesson at the end of the course schedule, followed by the Exercise.
# Note: Each time you Swap or Remove a lesson, you should do the same with the Exercises, if there are any following the lessons.
# Input / Constraints
#     • On the first line - the initial schedule lessons - strings, separated by comma and space ", ".
#     • Until "course start" you will receive commands in the format described above.
# Output
#     • Print the whole course schedule, each lesson on a new line with its number (index) in the schedule:
# "{lesson index}.{lessonTitle}".
#     • Allowed working time / memory: 100ms / 16MB.

initial_schedule = input().split(', ')

while True:
    input_command = input()
    if input_command == 'course start':
        break
    input_command = input_command.split(':')
    match input_command[0]:
        case 'Add':
            if input_command[1] not in initial_schedule:
                initial_schedule.append(input_command[1])
        case 'Insert':
            if input_command[1] not in initial_schedule:
                index = int(input_command[2])
                initial_schedule.insert(index, input_command[1])
        case 'Remove':
            if input_command[1] in initial_schedule:
                initial_schedule.remove(input_command[1])
        case 'Swap':
            if input_command[1] in initial_schedule and input_command[2] in initial_schedule:
                index_one = initial_schedule.index(input_command[1])
                index_two = initial_schedule.index(input_command[2])
                initial_schedule[index_one], initial_schedule[index_two] = initial_schedule[index_two], \
                initial_schedule[index_one]
                if f'{input_command[1]}-Exercise' in initial_schedule:
                    old_exercise_index = initial_schedule.index(f'{input_command[1]}-Exercise')
                    initial_schedule.pop(old_exercise_index)
                    new_exercise_index = initial_schedule.index(input_command[1]) + 1
                    initial_schedule.insert(new_exercise_index, f'{input_command[1]}-Exercise')

                elif f'{input_command[2]}-Exercise' in initial_schedule:
                    old_exercise_index = initial_schedule.index(f'{input_command[2]}-Exercise')
                    initial_schedule.pop(old_exercise_index)
                    new_exercise_index = initial_schedule.index(input_command[2]) + 1
                    initial_schedule.insert(new_exercise_index, f'{input_command[2]}-Exercise')

        case 'Exercise':
            if input_command[1] in initial_schedule and f'{input_command[1]}-Exercise' not in initial_schedule:
                lesson_index = initial_schedule.index(input_command[1])
                initial_schedule.insert(lesson_index + 1, f'{input_command[1]}-Exercise')
            elif input_command[1] not in initial_schedule:
                initial_schedule.append(input_command[1])
                initial_schedule.append(input_command[1] + '-Exercise')

for index, element in enumerate(initial_schedule, start=1):
    print(str(index) + '.' + element)