# On the first line, you will receive an integer number representing the next pair of rows.
# On the next lines, you will be receiving each student's name and their grade.
# Keep track of all grades for each student and keep only the students with an average grade higher than or equal to 4.50.
# Print the final dictionary with students and their average grade in the following format:
# "{name} -> {averageGrade}"
# Format the average grade to the 2nd decimal place.

total_pairs_of_rows = int(input())
grades_dict = {}

for student in range(total_pairs_of_rows):
    student_name = input()
    student_grade = float(input())
    if student_name not in grades_dict.keys():
        grades_dict[student_name] = [student_grade]
    else:
        grades_dict[student_name].append(student_grade)

for student in grades_dict.keys():
    average_grade = sum(grades_dict[student]) / len(grades_dict[student])
    if average_grade >= 4.50:
        print(f'{student} -> {average_grade:.2f}')


