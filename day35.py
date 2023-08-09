# Create a class called "Shape" with an instance attribute called "color". Implement a method called "display_color" that prints out the color of the shape.

# Create a child class called "Rectangle" that inherits from the "Shape" class. Add additional attributes called "length" and "width" to represent the dimensions of the rectangle. Implement a method called "calculate_area" that calculates and returns the area of the rectangle.

# Create a grandchild class called "Square" that inherits from the "Rectangle" class. Add an additional attribute called "side_length" to represent the length of each side of the square. Override the "calculate_area" method in the "Square" class to calculate and return the area of the square.

# Create an instance of the "Square" class with specific values for the color and side length. Call the "display_color" method to print out the color of the square. Then, call the "calculate_area" method to calculate and print out the area of the square.

# Parent class - Shape

class Shape:
    def __init__(self, color) -> None:
        self.color = color

    def display_color(self):
        print(f"Color: {self.color}")

# Child Class 1 - Rectangle

class Rectangle(Shape):
    def __init__(self, color, length , width) -> None:
        super().__init__(color)
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return f"Area of Rectangle: {self.length * self.width}"

# Child Class 2 - Square

class Square(Rectangle):
    def __init__(self, color, length, width, side_length) -> None:
        super().__init__(color, length, width)
        self.side_length = side_length
    
    def calculate_area(self):
        return f"Area of Square: {self.side_length ** 2}"

# Object for square
abcd = Square('red', 14, 5, 6)
print(abcd.calculate_area())
(abcd.display_color())

# Object for Rectangle
prqs = Rectangle('blue', 14, 5)
print(prqs.calculate_area())
