#1. Create a class called "Student" with attributes name, age, and marks. Implement a method to calculate and return the grade of the student based on the marks obtained. Create an instance of the class with some sample marks and print out the student's grade.

class Student:
    def __init__(self, name, age, marks) -> None:
        self.name = name
        self.age = age
        self.marks = marks
    def grade_obtained(self):
        if(self.marks <=100 and self.marks >=0):
            if(self.marks > 80):
                return "Grade A"
            elif(self.marks > 60):
                return "Grade B"
            elif(self.marks > 40):
                return "Grade C"
            else:
                return "Fail"
        else:
            return ('Please input the number ranging from 0 - 100')

You = Student('Arsalan', 13, 98)
You = Student('Arsalan', 13, 101)
print(You.grade_obtained())

    


#2. Create a class called "Circle" with attributes radius. Implement methods to calculate and return the area and circumference of the circle. Create an instance of the class and print out the area and circumference.
import math

class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius
    def area(self):
        return (self.radius)**2 * 22 / 7
    def cirfumference(self):
        return 2 * (22 / 7) * self.radius

a = Circle(5)
print(a.area())
print(a.cirfumference())