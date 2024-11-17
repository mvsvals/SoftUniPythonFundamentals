# Create a function that calculates and returns the area of a rectangle by a given width and height. Print the result on the console.

def rectangle_area(width: int, height: int) -> int:
    return width * height

input_width = int(input())
input_height = int(input())

print(rectangle_area(input_width, input_height))
