# --------------------- Polymorphism --------------------------


# ------------------- Question -------------------------

# Create a class called "Shape" with a method called "calculate_area". Create two subclasses "Circle" and "Rectangle", and override the "calculate_area" method in both subclasses. Demonstrate how polymorphism allows you to call the "calculate_area" method on objects of both subclasses using a loop.

# Parent Class

class Shape:
    def calculate_area(self):
        return 'The area of any x shape'

# Child Class - Circle

class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius

    def calculate_area(self):
        area  = (22 / 7) * (self.radius ** 2)
        return f"Area = {area}" 

# Child Class - Rectangle

class Rectangle(Shape):
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    
    def calculate_area(self):
        area = self.width * self.height
        return f"Area = {area}"


# Create an instance for Circle
circle = Circle(5)
# Create an instance for rectangle
rectangle = Rectangle(5, 10)

shapes = [circle, rectangle] 
# this shapes list now carries two object called circle and rectangle

for shape in shapes:
    print(shape.calculate_area())