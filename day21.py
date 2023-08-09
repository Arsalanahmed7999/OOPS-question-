#1 Create a class called "Employee" with attributes "name" and "salary". Create a child class called "Manager" that inherits from the "Employee" class. Add an attribute called "department" to the "Manager" class. Implement a method in the "Manager" class that prints out the name, salary, and department of the manager. Create an instance of the "Manager" class and call the method.

class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department) -> None:
        super().__init__(name, salary)
        self.department = department
    
    def info(self):
        return (f"The name is: {self.name}\nThe salary is: {self.salary}\nThe department is: {self.department}")

Arham = Manager('Arham', 20000, 'xyz department')
print(Arham.info())