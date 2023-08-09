# Heirarchical Inheritance

# Create a class called "Shape" with attributes "color" and "area". Implement a method called "calculate_area" that sets the "area" attribute based on the shape's properties. Create three child classes called "Circle", "Rectangle", and "Triangle", each inheriting from the "Shape" class.

# For the "Circle" class, add an additional attribute "radius". Implement the "calculate_area" method in the "Circle" class to calculate the area of the circle based on the given radius.

# For the "Rectangle" class, add additional attributes "width" and "height". Implement the "calculate_area" method in the "Rectangle" class to calculate the area of the rectangle based on the given width and height.

# For the "Triangle" class, add additional attributes "base" and "height". Implement the "calculate_area" method in the "Triangle" class to calculate the area of the triangle based on the given base and height.

# Create instances of the "Circle", "Rectangle", and "Triangle" classes with specific values for the attributes. Call the "calculate_area" method for each instance to calculate and set the area attribute. Then, print out the color, area, and specific attributes of each shape.

# Parent Class
class Shape:
    def __init__(self, color, area) -> None:
        self.color = color
        self.area = area
    
    def calculate_area(self):
        print(f"The area of the shape is {self.area}, and it's color is {self.color}")

# Child Class
class Circle(Shape):
    def __init__(self, color, area, radius) -> None:
        super().__init__(color, area)
        self.radius = radius
    
    def calculate_area(self):
        area = 22/7 * (self.radius ** 2)
        return f"Area of Circle: {area}"


# Child Class
class Rectangle(Shape):
    def __init__(self, color, area, width, height) -> None:
        super().__init__(color, area)
        self.width = width
        self.height = height
    
    def calculate_area(self):
        area = self.width * self.height
        return f"Area of Rectangle: {area}"


# Child Class
class Triangle(Shape):
    def __init__(self, color, area, base, height) -> None:
        super().__init__(color, area)
        self.base = base
        self.height = height
    
    def calculate_area(self):
        area =( 1/2) * (self.base) * (self.height)
        return f"Area of Triangle: {area}"


# Instance for Circle

a = Circle('blue', 0, 5)
print(a.calculate_area())
print(a.color)

# Instance for Rectangle

pqrs = Rectangle('yellow', 1242134123, 5, 6)
print(pqrs.calculate_area())
print(pqrs.color)

# Instance for Triangle
abc = Triangle('orange', 4213, 20, 10)
print(abc.calculate_area())
print(abc.color)