# --------------------- Polymorphism --------------------------


# ---------------------- Question -----------------------------

# Implement a function called "print_shapes" that takes a list of shape objects and calls their "print_info" method. Ensure that each shape class implements the "print_info" method differently to demonstrate polymorphism.

# Parent class
class Shape:
    def print_info(self):
        pass #This will be overriding

# Child class - square

class Square(Shape):
    def print_info(self):
        print('This is a square, it has 4 equal sides')
    
# Child class - rectangle

class Rectangle(Shape):
    def print_info(self):
        print('This is a rectangle, it has 4 sides and 2 of the opposite sides are equal sides.')

# Child class triangle

class Triangle(Shape):
    def print_info(self):
        print('This is a triangle, it has three sides')

# Child class Circle

class Circle(Shape):
    def print_info(self):
        print('This is a circle')

# instances

square = Square()
rectangle = Rectangle()
triangle = Triangle()
circle = Circle()


# List a of shape objects

shape_objects = [square, rectangle, triangle, circle]

# now running a loop 

for shape in shape_objects:
    shape.print_info()
    