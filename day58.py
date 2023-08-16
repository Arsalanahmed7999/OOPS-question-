# --------------------- Polymorphism --------------------------

# ---------------------- Question -----------------------------

# Create a class hierarchy with a base class "Employee" and subclasses "Manager" and "Developer". Implement a method called "calculate_salary" in each class. Demonstrate polymorphism by creating a list of "Employee" objects, including instances of both "Manager" and "Developer", and calling the "calculate_salary" method on each object.

# Parent Class Employee

class Employee:
    def __init__(self, name, role) -> None:
        self.name = name
        self.role = role
      
    def info(self):
        print(f'Name: {self.name}')
        print(f'Role: {self.role}')
    
    def calculate_salary(self):
        pass #We will be overriding this method 

# Child Class - Manager

class Manager(Employee):
    def __init__(self, name, role, salary) -> None:
        super().__init__(name, role)
        self.salary = salary
    
    def calculate_salary(self):
        print(f"Salary of {self.name} Manager: {self.salary}")

# Child Class - Developer

class Developer(Employee):
    def __init__(self, name, role, hourly_charge, hours_worked) -> None:
        super().__init__(name, role)
        self.hourly_charge = hourly_charge
        self.hours_worked = hours_worked
    
    def calculate_salary(self):
        salary = self.hourly_charge * self.hours_worked #(100 * 1000 = 100000)
        print(f"Salary of {self.name} Developer: {salary}")


# Creating Instances

manager1 = Manager('Ahmed', 'Manager', 50000)
manager2 = Manager('Arham', 'Manager', 70000)
manager3 = Manager('Rohit', 'Manager', 60000)

developer1 = Developer('Arsalan', 'Developer', 1000, 300)
developer2 = Developer('Shruti', 'Developer', 500, 200)
developer3 = Developer('Bilal', 'Developer', 2000, 400)
developer4 = Developer('Riya', 'Developer', 200, 9000)

# manager.calculate_salary()
# developer.calculate_salary()

listOfEmployees = [manager1, manager2, manager3, developer1, developer2, developer3, developer4]

# loop to calculate the salary for each indivudual object

for employee in listOfEmployees:
    employee.calculate_salary()