# --------------------- Polymorphism --------------------------


# ---------------------- Question -----------------------------

# Create a class hierarchy with a base class "Shape" and two subclasses "Circle" and "Rectangle". Implement a method called "calculate_area" in each class that calculates the area of the shape. Then, implement a function called "calculate_total_area" that takes a list of shape objects as input and calculates the total area. The function should use polymorphism to call the "calculate_area" method on each shape object, regardless of their specific subclass.

# Your task is to:

# Define a base class Shape with a method calculate_area that is meant to be overridden by subclasses.
# Create two subclasses, Circle and Rectangle, both inheriting from the Shape class. Override the calculate_area method in each subclass to calculate the area of the respective shapes.
# Implement a function calculate_total_area that takes a list of shape objects as input.
# Inside the function, iterate through the list of shape objects and call the calculate_area method on each object. Accumulate the calculated areas to calculate the total area.
# Return the total area.

# Parent Class

class Shape:
    def calculate_area(self):
        pass

# Child class Circle
class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius
    def calculate_area(self):
        area = 22 / 7 * (self.radius ** 2)
        return area

# Child Class Rectangle
class Rectangle(Shape):
    def __init__(self, width, height) -> None:
        super().__init__()
        self.width = width
        self.height = height
    
    def calculate_area(self):
        area = self.height * self.width
        return area


def calculate_total_area(shapes):
    total_area = 0
    for shape in shapes:
        total_area+=shape.calculate_area()
    return total_area


# Creating instances for circle and rectangle

circle = Circle(5) #78.57142857142857
circle1 = Circle(3) #28.285714285714285
rectangle = Rectangle(5, 10) #50
rectangle1 = Rectangle(2, 4) #8

# total area = 78.57 + 28.28 + 50 + 8

shape_list = [circle, circle1, rectangle, rectangle1]
total_area = calculate_total_area(shape_list)
print(f"Total Area : {total_area}")