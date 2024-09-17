from math import pi

class Shape:
    def area(self):
        return 0


def print_shape_area(shape: Shape):
    print(f"The area of the shape is: {shape.area()}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circle = Circle(5)
rectangle = Rectangle(4, 6)

print_shape_area(circle)
print_shape_area(rectangle)