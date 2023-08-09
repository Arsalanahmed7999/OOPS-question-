# Multilevel inheritance
# Create a class called "University" with attributes "name" and "location". Implement a method called "display_info" that prints out the name and location of the university.

# Create a child class called "College" that inherits from the "University" class. Add an additional attribute called "num_students" to represent the number of students in the college. Implement a method called "display_students" that prints out the number of students in the college.

# Create a grandchild class called "Department" that inherits from the "College" class. Add an additional attribute called "department_name" to represent the name of the department. Implement a method called "display_department" that prints out the name of the department.

# Create an instance of the "Department" class with specific values for the name, location, number of students, and department name. Call the "display_info", "display_students", and "display_department" methods to print out the information of the department.

# Parent Class
class University:
    def __init__(self, name, location) -> None:
        self.name = name
        self.location = location
    def display_info(self):
        print(f"Name: {self.name}\nLocation: {self.location}")

# Child class 1

class College(University):
    def __init__(self, name, location, num_students) -> None:
        super().__init__(name, location)
        self.num_students = num_students
    
    def display_students(self):
        print(f"Number of Students: {self.num_students}")

# Child Class 2

class Department(College):
    def __init__(self, name, location, num_students, department_name) -> None:
        super().__init__(name, location, num_students)
        self.department_name = department_name

    def display_department(self):
        print(f"Department Name: {self.department_name}")


a = Department('xname', 'ylocation', 1000, 'zdepartment')
(a.display_info())
(a.display_students())
(a.display_department())