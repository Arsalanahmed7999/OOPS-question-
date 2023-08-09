# Hybrid Inheritance:
# Hybrid inheritance is a combination of multiple types of inheritance.
# It can involve any combination of single, multiple, multilevel, or hierarchical inheritance.
# Example: A "Employee" class inheriting from a "Person" class using single inheritance and from an "Organization" class using multiple inheritance.



# Single Inheritance:
# Multiple Inheritance:
# Multilevel Inheritance:
# Hierarchical Inheritance:


#  ----------------------- BASIC STRUCTURE ----------------------------
# # Base class
# class Base:
#     def display_base(self):
#         print("This is the base class.")


# # Child class 1 inheriting from Base
# class Child1(Base):
#     def display_child1(self):
#         print("This is child class 1.")


# # Child class 2 inheriting from Base
# class Child2(Base):
#     def display_child2(self):
#         print("This is child class 2.")


# # Grandchild class inheriting from both Child1 and Child2
# class Grandchild(Child1, Child2):
#     def display_grandchild(self):
#         print("This is the grandchild class.")


# # Create an instance of the Grandchild class
# grandchild_obj = Grandchild()

# # Call methods of each class
# grandchild_obj.display_base()
# grandchild_obj.display_child1()
# grandchild_obj.display_child2()
# grandchild_obj.display_grandchild()



# -------------------------- QUESTION -----------------------------
# Create a base class called Shape. The Shape class should have a method called area() that returns 0.

# Create two derived classes called Rectangle and Circle.

# The Rectangle class should inherit from Shape and have additional attributes width and height. Implement the area() method in the Rectangle class to calculate and return the area of the rectangle.

# The Circle class should inherit from Shape and have an additional attribute radius. Implement the area() method in the Circle class to calculate and return the area of the circle.

# Finally, create a Square class that inherits from both Rectangle and Circle. The Square class should have an additional attribute side_length. Implement the area() method in the Square class to calculate and return the area of the square using the formula side_length ** 2.

# Parent Class

class Shape:
    def area(self):
        return 0

# Child class 1

class Rectangle(Shape):
    def __init__(self, width, height) -> None:
        super().__init__()
        self.width = width
        self.height = height
    def area(self):
        return self.height * self.width


# Child class 2
class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius
    
    def area(self):
        return 22/7 * (self.radius ** 2)

# Grandchild 

class Square(Rectangle, Circle):
    def __init__(self, side_length) -> None:
        self.side_length = side_length
    
    def area(self):
        return f"Area: {self.side_length ** 2}"

abcd = Square(4)
print(abcd.area())