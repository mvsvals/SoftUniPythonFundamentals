
employee_one_students_per_hour = int(input())
employee_two_students_per_hour = int(input())
employee_three_students_per_hour = int(input())
total_students_to_be_serviced = int(input())

remaining_students = total_students_to_be_serviced
hour = 0

while remaining_students > 0:
    hour += 1
    if hour % 4 == 0:
        continue
    remaining_students -= employee_one_students_per_hour + employee_two_students_per_hour + employee_three_students_per_hour

print(f'Time needed: {hour}h.')
