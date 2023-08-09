#1. Create a class called "BankAccount" with attributes account_number and balance. Create an instance of the class and deposit an amount of money into the account. Print out the current balance.

class BackAccount:
    def __init__(self, account_number, balance) -> None:
        self.account_number = account_number
        self.balance = balance

abc = BackAccount(8989786532212, 3000)
deposit = abc.balance
amount = int(input("Enter the amount you want to deposit into your bank account: \n"))
deposit+=amount
balance = deposit
print(f"You current balannce is : {balance}$")



#2. Create a class called "Student" with attributes name and grade. Create a method within the class that allows you to update the student's grade. Create an instance of the class and test the method by updating the student's grade.

class Student:
    def __init__(self, name, grade) -> None:
        self.name = name
        self.grade = grade
    
    def students_grade(self, new_grade):
        self.grade = new_grade

a = Student('Arsalan', 90)
print("The initial grade is", a.grade)
a.students_grade(80)
print("The updated grade is", a.grade)
