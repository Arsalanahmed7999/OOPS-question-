# -----------------Hybrid inheritance---------------------

# Create a class called "Person" with attributes "name" and "age". Implement a method called "display_info" that prints out the name and age of the person.

# Create two child classes called "Student" and "Employee", both inheriting from the "Person" class.

# For the "Student" class, add an additional attribute "student_id" to represent the student's ID. Implement a method called "display_student_id" that prints out the student's ID.

# For the "Employee" class, add an additional attribute "employee_id" to represent the employee's ID. Implement a method called "display_employee_id" that prints out the employee's ID.

# Create a grandchild class called "WorkingStudent" that inherits from both the "Student" and "Employee" classes.

# For the "WorkingStudent" class, add an additional attribute "salary" to represent the salary of the working student. Implement a method called "display_salary" that prints out the salary.

# Create an instance of the "WorkingStudent" class with specific values for the name, age, student ID, employee ID, and salary. Call the "display_info", "display_student_id", "display_employee_id", and "display_salary" methods to print out the information of the working student.

# In this question, you are using different classes: "Person" as the base class, "Student" and "Employee" as the child classes, and "WorkingStudent" as the grandchild class, demonstrating hybrid inheritance.

# Parent Class
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Child Class - Student

class Student(Person):
    def __init__(self, name, age, student_id) -> None:
        Person.__init__(self, name, age)
        # super.__init__(name, age)
        self.student_id = student_id
    
    def display_student_id(self):
        print(f"Student ID: {self.student_id}")


# Child Class - Employee

class Employee(Person):
    def __init__(self, name, age, employee_id) -> None:
        Person.__init__(self, name, age)
        self.employee_id = employee_id
        # super.__init__(name, age)
    
    def display_employee_id(self):
        print(f"Employee ID: {self.employee_id}")


# Grandchild - WorkingStudent

class WorkingStudent(Student, Employee): #(Student - parent1, Employee- parent2)
    def __init__(self, name, age, student_id, employee_id, salary) -> None:
        Student.__init__(self, name, age, student_id)
        Employee.__init__(self, name, age, employee_id)
        self.salary = salary
    def display_salary(self):
        print(f"Salary: {self.salary}Rs")

# Create an intance for our working student class

arsalan = WorkingStudent('Arsalan', 24, 5034056789, 1908, 20000)
arsalan.display_info() #This belongs to person class
arsalan.display_student_id() #This belongs to student class
arsalan.display_employee_id() #This belongs to employee class
arsalan.display_salary() #This belongs to workingstudent class