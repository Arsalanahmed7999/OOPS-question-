# Multiple Inheritance:

# In multiple inheritance, a class can inherit from multiple parent classes.
# It allows a class to inherit attributes and methods from multiple base classes.
# Example: A "Student" class inheriting from both a "Person" class and a "Scholar" class.

# Single Inheritance:
# Multilevel Inheritance:
# Hierarchical Inheritance:
# Hybrid Inheritance:
# --------------------------------------------
# 1. Create two parent classes, "A" and "B", with a method called "display" that prints a message specific to each class.

# Create a child class called "C" that inherits from both "A" and "B". Implement a method called "show" in the "C" class that calls the "display" method of both parent classes. Create an instance of the "C" class and call the "show" method.

class Scholar: #parent class 1
    pass
class Person: #parent class 2
    pass
class Student(Scholar, Person): #child class inheriting from the parent class 
    pass

#parent class 1
class A:
    def display_A(self):
        print('This is A')
#parent class 2
class B:
    def display_B(self):
        print('This is B')
#child class
class C(A, B):
    def show(self):
        self.display_A()
        self.display_B()
# The first parameter in the child class class in multiple inheritance will be given more preference
c = C()
c.show()
