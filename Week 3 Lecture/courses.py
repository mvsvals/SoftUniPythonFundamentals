# On the first line, you will receive a single number n.
# On the following n lines, you will receive names of courses.
# You should create a list of courses and print it.


input_number = int(input())
course_list = []

for _ in range(input_number):
    course_input = input()
    course_list.append(course_input)

print(course_list)