# --------------------- Abstraction -----------------------------



# --------------------- Question --------------------------------

# You are developing a geometry application that needs to calculate the area of various shapes. Implement an abstract class called "Shape" with an abstract method "calculate_area". This abstract class will serve as the base for different types of shapes. Create two subclasses, "Circle" and "Rectangle", that inherit from the "Shape" class. Each subclass should provide its own implementations for calculating the area based on its specific attributes.

# parent class
from abc import ABC, abstractmethod
class Shapes(ABC): #this is an abstract class which was a concrete first 
    @abstractmethod #this is also an abstract method which was a concrete first 
    def calculate_area(self):
        pass

# Child class Circle

class Circle(Shapes): #this is a concrete class 
    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius

    def info(self):
        print('This is a circle')
    
    def calculate_area(self):
        area = (22 / 7) * self.radius ** 2
        return area
    
class Rectangle(Shapes): #this is a concrete class 
    def __init__(self, width, height) -> None:
        super().__init__()
        self.width = width
        self.height = height

    def info(self):
        print('This is a rectangle')
    
    def calculate_area(self):
        area = self.width * self.height
        return area
    
class Square(Shapes): #this is a concrete class 
    def __init__(self, side) -> None:
        super().__init__()
        self.side = side


    def info(self):
        print('This is a square')
    
    def calculate_area(self):
        area = self.side ** 2
        return area
    
    


circle = Circle(5)
circle.info()
print(circle.calculate_area())

rectangle = Rectangle(5, 10)
rectangle.info()
print(rectangle.calculate_area())

square = Square(8)
square.info()
print(square.calculate_area())