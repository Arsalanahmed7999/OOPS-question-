# Multilevel Inheritance:
# In multilevel inheritance, a class can inherit from a derived class, which itself is derived from another class.
# It creates a hierarchical structure of inheritance.
# Example: A "Grandchild" class inheriting from a "Child" class, which in turn inherits from a "Parent" class.


# Multiple Inheritance:
# Single Inheritance:
# Hierarchical Inheritance:
# Hybrid Inheritance:

# # Parent class
# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def display_parent(self):
#         print(f"Parent: {self.name}")


# # Child class inheriting from Parent
# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age

#     def display_child(self):
#         print(f"Child: {self.name}, Age: {self.age}")


# # Grandchild class inheriting from Child
# class Grandchild(Child):
#     def __init__(self, name, age, hobby):
#         super().__init__(name, age)
#         self.hobby = hobby

#     def display_grandchild(self):
#         print(f"Grandchild: {self.name}, Age: {self.age}, Hobby: {self.hobby}")


# # Create an instance of the Grandchild class
# grandchild = Grandchild("John", 12, "Playing Guitar")

# # Call methods to display information at each level of inheritance
# grandchild.display_grandchild()
# grandchild.display_child()
# grandchild.display_parent()


# Create a class called Animal with an attribute species. Implement a method called display_species that prints out the species of the animal.

# Create a child class called Mammal that inherits from the Animal class. Add an additional attribute milk_production to the Mammal class. Implement a method called display_milk_production that prints out the milk production ability of the mammal.

# Create a grandchild class called Human that inherits from the Mammal class. Add an additional attribute name to the Human class. Implement a method called display_info that prints out the name, species, and milk production ability of the human.

# Create an instance of the Human class with a specific name, species, and milk production ability. Call the display_info method to print out the information of the human.

# Parent Class
class Animal:
    def __init__(self, species) -> None:
        self.species = species
    def display_species(self):
        return f"The species is: {self.species}"
    
# Child class 1

class Mammal(Animal):
    def __init__(self, species, milk_production) -> None:
        super().__init__(species)
        self.milk_production = milk_production
    
    def display_milk_production(self):
        return f"The Milk Production: {self.milk_production}"

# Child Class 2

class Human(Mammal):
    def __init__(self, species, milk_production, name) -> None:
        super().__init__(species, milk_production)
        self.name = name
    def display_name(self):
        return f"The Name: {self.name}"

# elephant = Mammal('speiciesX', 12)
# print(elephant.display_species())
# print(elephant.display_milk_production())

Arsalan = Human('Species Y', 15, 'Arsalan')
print(Arsalan.display_name())

