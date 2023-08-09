# Hierarchical Inheritance:

# In hierarchical inheritance, multiple classes inherit from a single base class.
# It forms a tree-like structure of inheritance.
# Example: "Cat", "Dog", and "Lion" classes inheriting from an "Animal" class.

# Single Inheritance:
# Multiple Inheritance:
# Multilevel Inheritance:
# Hybrid Inheritance:

# BASIC STRUCTURE
# Parent Class 

# class Animal:
#     def __init__(self, species, sound):
#         self.species = species
#         self.sound = sound

#     def make_sound(self):
#         print(f"The {self.species} makes a {self.sound} sound.")

# # Child Class
# class Cat(Animal):
#     def __init__(self, name, sound):
#         super().__init__("cat", sound)
#         self.name = name

# # Child Class
# class Dog(Animal):
#     def __init__(self, name, sound):
#         super().__init__("dog", sound)
#         self.name = name

# class Horse(Animal):
#     pass

# class Cow(Animal):
#     pass

# cat = Cat("Fluffy", "meow")
# cat.make_sound()

# dog = Dog("Buddy", "bark")
# dog.make_sound()

# In this code, we have a base class called Animal with attributes "species" and "sound", along with a method called "make_sound" to display the sound of the animal. Then, we have two child classes, Cat and Dog, that inherit from the Animal class. Each child class has an additional attribute "name" and overrides the "species" attribute with the specific animal name (i.e., "cat" and "dog"). When we create instances of the child classes and call the "make_sound" method, it will display the specific sound of the cat and dog respectively.



# ----------------- QUESTION -----------------
# Create a class called "Shape" with an attribute "name". Implement a method called "display_info" that prints out the name of the shape.

# Create two child classes, "Circle" and "Square", both inheriting from the "Shape" class. Add an additional attribute "radius" to the "Circle" class and "side_length" to the "Square" class.

# Create instances of both child classes and set specific values for the "name", "radius", and "side_length" attributes. Call the "display_info" method for each instance to print out the name of the shape.

# Parent Class
class Shape:
    def __init__(self, name) -> None:
        self.name = name
    
    def display_info(self):
        print(f"Name: {self.name}")


# Child Class 

class Square(Shape):
    def __init__(self, name, side_length) -> None:
        super().__init__(name)
        self.side_length = side_length


# Child Class 

class Circle(Shape):
    def __init__(self, name, radius) -> None:
        super().__init__(name)
        self.radius = radius


abcd = Square('abcd-Square', 5)
abcd.display_info()
y = Circle('y-Circle', 10)
y.display_info()
# print(y.radius)

