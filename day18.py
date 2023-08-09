#1 Create a class called "Shape" with an attribute called "color". Create a child class called "Circle" that inherits from the "Shape" class. Add an attribute called "radius" to the "Circle" class. Create an instance of the "Circle" class and print out the color and radius of the circle.

class Shape:
    def __init__(self, color) -> None:
        self.color = color

class Circle(Shape):
    def __init__(self, color, radius) -> None:
        super().__init__(color)
        self.radius = radius

a = Shape('blue')
print(a.color)
b = Circle('red', 5)
print(f"The color is {b.color}, and the radius of circle is {b.radius} cm^2")