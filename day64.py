# -------------------- Encapsulation ---------------------

#  -------------------- Question --------------------------

# Define a class called "Employee" with private attributes "name", "salary", and "employee_id". Implement a method to calculate a bonus based on the salary. Demonstrate the encapsulation concept by calling the method to calculate and apply the bonus.

class Employee:
    def __init__(self, name, salary, employee_id) -> None:
        self.__name = name #private attribute
        self.__salary = salary #private attribute
        self.__employee_id = employee_id #private attribute
    
    def calculate_bonus(self, percentage):
        bonus = (percentage / 100) * self.__salary # 5% -> 5 / 100 -> 0.05 * 10000 -> 500
        return bonus
    
    def get_name(self):
        return self.__name
    
    def get_salary(self):
        return self.__salary

    def get_employee_id(self):
        return self.__employee_id


Arsalan = Employee('Arsalan', 10000, 1094)
print(Arsalan.get_name())
print(Arsalan.get_salary())
print(Arsalan.get_employee_id())
# print(Arsalan.__name)

print(Arsalan.calculate_bonus(5))





