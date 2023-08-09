#1. Create two parent classes, "Person" and "Employee", with attributes and methods specific to each class, such as "get_name" in "Person" and "calculate_salary" in "Employee".

# Create a child class called "Manager" that inherits from both "Person" and "Employee". Implement a method called "display_info" in the "Manager" class that calls the methods from both parent classes to get the name and calculate the salary. Create an instance of the "Manager" class and call the "display_info" method.

# Parent Class 1

class Person:
    def __init__(self, name) -> None:
        self.name = name
    def get_name(self):
        return self.name


# Parent Class 2

class Employee:
    def __init__(self, salary) -> None:
        self.salary = salary
    def calculate_salary(self):
        return self.salary

# Child Class 

class Manager(Person, Employee):
    def __init__(self, name, salary) -> None:
        Person.__init__(self, name)
        Employee.__init__(self, salary)
    
    def display_info(self):
        salary = self.calculate_salary()
        name = self.get_name()
        print(f'The name of the manager is {name} and the salary is {salary}')

Ahmed = Manager('Ahmed', 20000)
Ahmed.display_info()






