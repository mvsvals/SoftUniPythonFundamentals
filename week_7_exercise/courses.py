course_dict = {}

while True:
    input_string = input()
    if input_string == 'end':
        break
    course_name, student_name = input_string.split(" : ")
    if course_name not in course_dict.keys():
        course_dict[course_name] = []
    course_dict[course_name].append(student_name)

for course in course_dict.keys():
    print(f"{course}: {len(course_dict[course])}")
    for student in course_dict[course]:
        print('-- ' + student)
