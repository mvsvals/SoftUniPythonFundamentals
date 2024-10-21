import math

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
biggest_bonus, biggest_attendance = 0, 0

for student in range(number_of_students):
    attendance_of_student = int(input())
    total_bonus = attendance_of_student / number_of_lectures * (5 + additional_bonus)
    if total_bonus >= biggest_bonus:
        biggest_bonus = total_bonus
        biggest_attendance = attendance_of_student

print(f"Max Bonus: {math.ceil(biggest_bonus)}.")
print(f"The student has attended {math.ceil(biggest_attendance)} lectures.")
