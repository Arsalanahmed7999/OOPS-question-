# --------------------- Abstraction -----------------------------



# --------------------- Question --------------------------------

# Create an abstract class called "Shape" with an abstract method called "calculate_area". Create two subclasses, "Rectangle" and "Circle", that inherit from "Shape" and provide their own implementations for calculating area.

from abc import ABC, abstractmethod
class Shape(ABC): #abstract class 
    @abstractmethod 
    def calculate_area(self): #abstract method 
        pass

class Rectangle(Shape):
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    def calculate_area(self):
        area = self.width * self.height
        print(f'Area of rectangle: {area}')

class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius
    def calculate_area(self):
        area = (22 / 7) * (self.radius ** 2)
        print(f"The Area of a Circle: {area}")


# a = Shape() #we cannot create an instance for our abstract class 
# print(a.calculate_area())


rectangle = Rectangle(4, 5)
rectangle.calculate_area()


circle = Circle(5)
circle.calculate_area()