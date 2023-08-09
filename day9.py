#1. Create a class called "Student" with attributes name, grade, and subjects. Implement a method called add_subject that allows you to add a new subject to the student's list of subjects. Implement another method called get_subjects that returns the list of subjects. Create an instance of the class with a sample name and grade. Use the add_subject method to add a few subjects to the student's list. Finally, use the get_subjects method to retrieve and print the list of subjects.

class Student:
    def __init__(self, name, grade, subjects) -> None:
        self.name = name
        self.grade = grade
        self.subjects = subjects

    def add_subject(self, new_subject):
        self.subjects.append(new_subject)
    
    def get_subjects(self):
        return self.subjects

Ahmed = Student('Ahmed', "A", ['English', 'Mathematics', 'Urdu', 'Science', 'Hindi'])
print(Ahmed.name)
print(Ahmed.grade)
print(Ahmed.get_subjects())
(Ahmed.add_subject('French'))
print(Ahmed.get_subjects())
