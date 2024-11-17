# Calculate how many courses will be needed to elevate N persons by using an elevator capacity of P persons.
# The input holds two lines: the number of people N and the capacity P of the elevator.

import math

total_people = int(input())
elevator_capacity = int(input())

total_courses_needed = math.ceil(total_people / elevator_capacity)
print(total_courses_needed)