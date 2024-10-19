import math


# Base Class - Shape
class Shape:
    def area(self):
        # Raising an error because derived classes should implement this method
        raise NotImplementedError("Subclasses must override the area() method")


# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # Overrides area method to calculate area of rectangle
        return self.length * self.width


# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Overrides area method to calculate area of circle
        return math.pi * (self.radius**2)


# Test polymorphism by using different shapes
def polymorphism_demo():
    # Create instances of Rectangle and Circle
    shapes = [Rectangle(5, 3), Circle(7)]

    # Iterate through the shapes and print their areas
    for shape in shapes:
        print(f"The area of the {type(shape).__name__} is: {shape.area():.2f}")


if __name__ == "__main__":
    polymorphism_demo()
