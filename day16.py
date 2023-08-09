# @classmethod is used to define a method that operates on the class itself rather than an instance of the class.

# When a method is decorated with @classmethod, it receives the class itself as the first argument, conventionally named cls (similar to self for instance methods). This allows the method to access and modify class-level attributes or perform operations related to the class as a whole, rather than individual instances.

# The @classmethod decorator is commonly used when you want to define methods that deal with class-level operations, such as creating class-level attributes, accessing class-level data, or performing class-specific computations.

# Here's an example to illustrate the usage of @classmethod:

# class MyClass:
#     class_attribute = 10

#     def __init__(self, instance_attribute):
#         self.instance_attribute = instance_attribute

#     @classmethod
#     def class_method(cls):
#         print("Class attribute:", cls.class_attribute)

#     def instance_method(self):
#         print("Instance attribute:", self.instance_attribute)


# # Accessing class-level method using @classmethod

# MyClass.class_method()
# # Creating an instance of MyClass
# obj = MyClass(20)

# # Accessing instance-level method
# obj.instance_method()


# In the example, the class_method is decorated with @classmethod, allowing it to access the class attribute class_attribute. The method is called on the class itself, not on an instance of the class. The instance_method, on the other hand, is an instance-level method and can only be called on instances of the class.

# The @classmethod decorator helps distinguish between methods that operate on the class (class methods) and methods that operate on individual instances (instance methods).



# 1. Create a class called "Company" with a class-level attribute called "employee_count" that represents the total count of employees in the company. The attribute should be initialized to 0 and incremented every time a new employee object is created.

# The Company class should also have instance attributes for "name" and "position" to represent the name and position of each employee.

# Create three instances of the Company class with different employee names and positions. After creating the instances, print out the total count of employees using the class-level attribute.

class Company:
    employee_count = 0

    def __init__(self, name, position) -> None:
        self.name = name
        self.position = position
        Company.employee_count+=1
        # every time an object or an instance is created that means that def init or you can that the object is created. So question asks us to increment the employee count by 1 everytime an object is created.
    
    @classmethod
    def get_employee_count(cls):
        print('The employee count', cls.employee_count)



print(Company.employee_count)
company1 = Company('tesla', 'manager')
print(Company.employee_count)
company2 = Company('tata', 'manager')
print(Company.employee_count)
company3 = Company('mahindra', 'manager')
print(Company.employee_count)

Company.get_employee_count()
# I want or create a method or a fucntion where I write just the name of the method and I get the employee count.





