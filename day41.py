# Heirarchical Inheritance

# Create a class called "Employee" with attributes "name" and "designation". Implement a method called "display_info" that prints out the name and designation of the employee.

# Create two child classes, "Manager" and "Engineer", both inheriting from the "Employee" class. Add an additional attribute "department" to the "Manager" class and "specialization" to the "Engineer" class.

# Create instances of both child classes and set specific values for the "name", "designation", "department", and "specialization" attributes. Call the "display_info" method for each instance to print out the name and designation of the employee.

# Parent Class
class Employee:
    def __init__(self, name, designation) -> None:
        self.name = name
        self.designation = designation
    
    def display_info(self):
        print(f'Name: {self.name}')
        print(f'Designation: {self.designation}')
    
# Child Class 
class Manager(Employee):
    def __init__(self, name, designation, department) -> None:
        super().__init__(name, designation)
        self.department = department

# Child Class 
class Engineer(Employee):
    def __init__(self, name, designation, specialization) -> None:
        super().__init__(name, designation)
        self.specialization = specialization


# Instance for Manager

Arsalan = Manager('Arsalan', 'Manager', 'xdepartment')
Arsalan.display_info()


print()
print()
print()
print()
# Instance for Engineer

Ahmed = Engineer('Ahmed', 'Engineer', 'ydepartment')
Ahmed.display_info()