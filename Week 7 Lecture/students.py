# You will be receiving names of students, their ID, and a course of programming they have taken in the format "{name}:{ID}:{course}".
# On the last line, you will receive the name of a course in snake case lowercase letters.
# You should print only the information of the students who have taken the corresponding course in the format: "{name} - {ID}" on separate lines.

search_course = ''
student_database = []

while True:
    input_string = input()
    if ':' not in input_string:
        search_course = input_string.replace('_', ' ')
        break
    name, id, course = input_string.split(':')
    student_database.append({'name': name, 'id': id, 'course': course})

for index, student in enumerate(student_database):
    if search_course in student.values():
        print(f"{student['name']} - {student['id']}")