#1. Create a class called "Person" with attributes name and age. Create an instance of the class and print out the person's name and age.

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

Arsalan = Person('Arsalan', 22)
print(f"My name is {Arsalan.name}, My age is {Arsalan.age}")
# print(f"My age is {Arsalan.age}")


#2. Create a class called "Car" with attributes make, model, and year. Create an instance of the class and print out the car's make, model, and year.

class Car:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year

car1 = Car('Honda', 'City', 2022)        
print(car1.make, car1.model, car1.year)

#3. Create a class called "Circle" with an attribute radius. Create an instance of the class and calculate the area of the circle using the formula (pi * radius^2).

class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

a = Circle(5)
pi = 22 / 7
area = f"The area is {(round((pi) * (a.radius ** 2 )))} unit^2"
print(area)
