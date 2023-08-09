#1 Create a class called "School" with a class-level attribute "school_name" that represents the name of the school. The attribute should be initialized to an empty string.

# The School class should also have instance attributes for "student_count" and "teacher_count" to represent the number of students and teachers in the school. These attributes should be initialized to 0.

# Implement instance methods for adding students and teachers to the school, as well as a method to print out the total number of students and teachers.

# Create three instances of the School class with different student and teacher counts. Add students and teachers to the school instances. Change the school name using the class-level method.

class School:
    school_name = "" #class level attribute

    def __init__(self) -> None:
        self.student_count = 0
        self.teacher_count = 0
    
    def add_student(self):
        self.student_count+=1

    def add_teacher(self):
        self.teacher_count+=1
    
    @classmethod #class method its a decorator 
    def add_school_name(cls, name):
        cls.school_name = name

    

school1 = School()
print(school1.school_name)
(school1.add_school_name('school1'))
print(school1.school_name)
print('student count', school1.student_count)
print('teacher count', school1.teacher_count)

# we are running the methods to increment the teacher count and student count

school1.add_student()
school1.add_teacher()
print('student count', school1.student_count)
print('teacher count', school1.teacher_count)
school2 = School()
school3 = School()

    
