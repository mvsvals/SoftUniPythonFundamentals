# You will be given the coordinates of two points on a Cartesian coordinate system - X1, Y1, X2, and Y2 on separate lines.
# Write a function that prints the point which is closest to the center of the coordinate system (0, 0) in the format: "({X}, {Y})"
# If the points are at the same distance from the center, print only the first one. The resulting coordinates must be formatted to the lower integer.

import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

def determine_distance(x1: float, y1: float, x2: float, y2: float) -> str:
    first_point_coordinates = [abs(x1), abs(y1)]
    second_point_coordinates = [abs(x2), abs(y2)]
    if sum(first_point_coordinates) < sum(second_point_coordinates) or sum(first_point_coordinates) == sum(second_point_coordinates):
        return '(' +str(math.floor(x1)) + ", " + str(math.floor(y1)) + ')'
    else:
        return '(' + str(math.floor(x2)) + ", " + str(math.floor(y2)) + ')'

print(determine_distance(x1, y1, x2, y2))




