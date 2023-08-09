#1 Create a class called "Student" with attributes name and grades. Implement a method to calculate and return the average grade of the student. The grades attribute should be a list of numerical grades. Create an instance of the class with a sample name and grades. Use the method to calculate the average grade and print out the result.


class Student:
    def __init__(self, name, grades) -> None:
        self.name = name
        self.grades = grades
    def average_grades(self):
        return f"The average grades of {self.name} is {sum(self.grades) / len(self.grades)}"


# grades = [ 80, 70, 50, 40, 90, 75, 54 ]

Ahmed = Student('Ahmed', [ 80, 70, 50, 40, 90, 75, 54 ])
Arsalan = Student('Arsalan', [1,2,3])
print(Ahmed.name)
print(Ahmed.grades)
print(Ahmed.average_grades())
print(Arsalan.average_grades())


# Average is?
# grades = [ 80, 70, 50, 40, 90, 75, 54 ]
# average = (80 + 70 + 50 + 40 + 90) / 7


# l1 = [1,2,3] 
# # (1 + 2 + 3) / 3 = 2
# average = sum(l1)/len(l1)
# print(average)