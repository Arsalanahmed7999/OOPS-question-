# Single Inheritance:
# In single inheritance, a class inherits from a single parent class.
# It forms a "is-a" relationship between the derived class (child) and the base class (parent).
# Example: A "Car" class inheriting from a "Vehicle" class.

# Multiple Inheritance:
# Multilevel Inheritance:
# Hierarchical Inheritance:
# Hybrid Inheritance:

#1 Create a class called "Person" with attributes name and age. Create a child class called "Student" that inherits from the "Person" class. Add an attribute called "grade" to the "Student" class. Create an instance of the "Student" class and print out the name, age, and grade.

class Person: #parent class
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

class Student(Person): #child class whose name is Student
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

# super keyword or a built in function means that we can use the instance attribute or functions of the parent class 



Ahmed = Person('Ahmed', 24)
print(Ahmed.name)

Arsalan = Student('Arsalan', 30, 10) #this is an instance of a child class
print(f"The name of the student is {Arsalan.name}, his age is {Arsalan.age} and his grade is {Arsalan.grade}")