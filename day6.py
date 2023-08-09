#1. Create a class called "Employee" with attributes name, position, and salary. Implement a method to calculate and return the annual salary of the employee. Create an instance of the class with a sample name, position, and monthly salary. Print out the annual salary of the employee.

class Employee:
    def __init__(self, name, position, salary) -> None:
        self.name = name
        self.position = position
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12
    
Arsalan = Employee('Arsalan', "Junior Developer", 12000) #this is an instance or you even say this is an object
Ahmed = Employee('Ahmed', "Manager", 30000) #this is an instance or you even say this is an object
print(Arsalan.annual_salary())
print(Ahmed.annual_salary())
print(Arsalan.name)
print(Arsalan.position)


#2. Create a class called "Triangle" with attributes base and height. Implement a method to calculate and return the area of the triangle using the formula (base * height) / 2. Create an instance of the class with given base and height, and print out the area of the triangle.


class Triangle:
    def __init__(self, base, height) -> None:
        self.base = base 
        self.height = height
    
    def area(self):
        return f"The area of Triangle is {(self.height * self.base ) / 2} unitsquare"


abc = Triangle(10, 10)
print(abc.area())
pqr =Triangle(3, 20)
print(pqr.area())
print(abc.base)