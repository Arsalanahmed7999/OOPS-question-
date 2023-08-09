#1 Create a class called "Person" with attributes "name" and "age". Implement a method called "display_info" that prints out the name and age of the person.

# Create a child class called "Student" that inherits from the "Person" class. Add an additional attribute called "student_id" to the "Student" class. Implement a method called "display_student_info" that prints out the name, age, and student ID of the student.

# In the "Student" class, add a list attribute called "courses" to store the names of the courses the student is enrolled in. Implement methods to add a course to the list, remove a course from the list, and display all the courses the student is enrolled in.

# Create an instance of the "Person" class and set the name and age attributes. Call the "display_info" method to print out the name and age of the person.

# Create an instance of the "Student" class and set the name, age, student ID, and initial courses attributes. Call the "display_info" method inherited from the "Person" class to print out the name and age of the student. Then, call the "display_student_info" method to print out the name, age, and student ID of the student.

# Add some additional courses using the method to add a course. Remove a course using the method to remove a course. Finally, call the method to display all the courses the student is enrolled in.

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def display_info(self):
        return (f"The name of person is {self.name} and age is {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id, courses) -> None:
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = courses
    def display_student_info(self):
        return f"The name of the studetn is {self.name}, the age is {self.age} and the studentID is {self.student_id}"
    
    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print('There is no such course in the enrolled courses')
    
    def display_enrolled_courses(self):
        
        for course in self.courses:
            print(course)
    
    
Arsalan = Person('Arsalan', 56)
print(Arsalan.display_info())

# 4 attributes for student
Ahmed = Student('Ahmed', 15, 402, ['English', 'Mathematics', 'Hindi'])
print(Ahmed.display_student_info())

Ahmed.add_course('French')
(Ahmed.display_enrolled_courses())
Ahmed.remove_course('Hindi')
(Ahmed.display_enrolled_courses())
