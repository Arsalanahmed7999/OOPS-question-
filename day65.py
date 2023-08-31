# -------------------- Encapsulation ---------------------

#  -------------------- Question --------------------------

# Design a class called "Student" with private attributes "name", "age", and "courses_taken" (a list of courses). Implement methods to add courses to the student's course list and to display the student's information. Demonstrate encapsulation by creating a student object, adding courses, and displaying the student's information.

class Student:
    def __init__(self, name, age, courses_taken) -> None:
        self.__name = name #private attribute
        # self.name = name #public attribute
        self.__age = age #private attribute
        self.__courses_taken = courses_taken #private attribute
    
    def add_courses(self, course):
        self.__courses_taken.append(course)
    
    def info(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"Courses Takes: {self.__courses_taken}")


ahmed = Student('Ahmed', 16, ['Mathematic', 'English', 'French', 'Science'])
# print(ahmed.__name)
# print(ahmed.name)
ahmed.info()

print()
ahmed.add_courses('Urdu')

ahmed.info()