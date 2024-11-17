# You will be given the coordinates of four points.
# The first and the second pair of points form two different lines.
# Create a function that prints the longer line in the format:
# "({X1}, {Y1})({X2}, {Y2})"
# starting from the point which is closer to the center of the coordinate system (0, 0).
# You can reuse the method that you wrote for the previous problem.
# If the lines are of equal length, print only the first one.
# The resulting coordinates must be formatted to the lower integer.

import math
# Line 1
line_one_first_point = [float(input()), float(input())]
line_one_second_point = [float(input()), float(input())]

# Line 2
line_two_first_point = [float(input()), float(input())]
line_two_second_point = [float(input()), float(input())]

def determine_longest_line(l1_first_point, l1_second_point, l2_first_point, l2_second_point):
    line_one_distance = math.sqrt((line_one_second_point[0] - line_one_first_point[0]) ** 2 + (line_one_second_point[1] - line_one_first_point[1]) ** 2)
    line_two_distance = math.sqrt((line_two_second_point[0] - line_two_first_point[0]) ** 2 + (line_two_second_point[1] - line_two_first_point[1]) ** 2)
    if line_one_distance >= line_two_distance:
        determine_distance(line_one_first_point[0], line_one_first_point[1], line_one_second_point[0], line_one_second_point[1])
    else:
        determine_distance(line_two_first_point[0], line_two_first_point[1], line_two_second_point[0], line_two_second_point[1])


def determine_distance(a1: float, b1: float, a2: float, b2: float) -> str:
    first_point_coordinates = [abs(a1), abs(b1)]
    second_point_coordinates = [abs(a2), abs(b2)]
    if sum(first_point_coordinates) < sum(second_point_coordinates) or sum(first_point_coordinates) == sum(second_point_coordinates):
        print('(' + str(math.floor(a1)) + ", " + str(math.floor(b1)) + ')' + '(' + str(math.floor(a2)) + ", " + str(math.floor(b2)) + ')')
    else:
        print('(' + str(math.floor(a2)) + ", " + str(math.floor(b2)) + ')' + '(' + str(math.floor(a1)) + ", " + str(math.floor(b1)) + ')')

determine_longest_line(line_one_first_point, line_one_second_point, line_two_first_point, line_two_second_point)

