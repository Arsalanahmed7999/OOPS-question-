#1. Create a class called "Rectangle" with attributes length and width. Implement a method to calculate and return the area of the rectangle. Create an instance of the class and print out the area.

class Rectangle:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        return area

a = Rectangle(5, 6)
print(a.area())


#2. Create a class called "Employee" with attributes name, designation, and salary. Implement a method that displays the employee's details (name, designation, and salary) as a formatted string. Create an instance of the class and call the method to display the employee's details.

class Employee:
    def __init__(self, name, designation, salary) -> None:
        self.name = name
        self.designation = designation
        self.salary = salary
    def display_info(self):
        return f"My name is {self.name}, my designation is {self.designation} and my salary is {self.salary}$"

Ahmed = Employee('Ahmed', 'Manager', 50000)
print(Ahmed.display_info())