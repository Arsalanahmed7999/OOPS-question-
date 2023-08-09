# Create a class called "Person" with attributes "name" and "age". Implement a method called "display_info" that prints out the name and age of the person.

# Create a child class called "Employee" that inherits from the "Person" class. Add an additional attribute called "employee_id" to the "Employee" class. Implement a method called "display_employee_info" that calls the "display_info" method from the parent class and prints out the employee ID.

# Create a grandchild class called "Manager" that inherits from the "Employee" class. Add an additional attribute called "department" to the "Manager" class. Implement a method called "display_manager_info" that calls the "display_employee_info" method from the parent class and prints out the department of the manager.

# Create an instance of the "Manager" class with specific values for the name, age, employee ID, and department. Call the "display_manager_info" method to print out the information of the manager.

# Person - Parent Class

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name:{self.name}\nAge: {self.age}")
    
# Child class 1 - Employee

class Employee(Person):
    def __init__(self, name, age, employee_id) -> None:
        super().__init__(name, age)
        self.employee_id = employee_id
    
    def display_employee_info(self):
        self.display_info()
        print(f"Employee ID: {self.employee_id}")
    
# Child class 2 - Maanger
class Manager(Employee):
    def __init__(self, name, age, employee_id, department) -> None:
        super().__init__(name, age, employee_id)
        self.department = department
    
    def display_manager_info(self):
        self.display_employee_info()
        print(f"Department: {self.department}")
    
# Creating an object now

Ahmed = Manager('Ahmed', 31, 5145, 'IT sector')
(Ahmed.display_manager_info())