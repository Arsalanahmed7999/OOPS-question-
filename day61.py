# -------------------- Encapsulation ---------------------


# Encapsulation is like putting your things in a box to keep them safe and organized. In programming, it means putting data (like numbers or names) and actions (like calculating or changing things) related to a thing together in one place called a "class".

# Imagine you have a box with your favorite toy inside it. The box hides the toy and lets you play with it using the box's handle. In a similar way, encapsulation hides the details of how things work inside a class and provides methods (like handles) to interact with them.

# For example, think about a "Person" class. It can have private things like a person's name and age. With encapsulation, we put these private things inside the class and use special methods (like "get" and "set" methods) to read or change them. This way, we control how these things are used and changed, making sure they are accurate and safe.

# So, encapsulation is like keeping your things organized and safe in a box (class), and you interact with them using methods (handles) provided by the class. This helps in keeping the code easy to manage and understand.


# -------------------------- Basic Structure -------------------------
class ClassName:
    def __init__(self, name):
        self.__private_attribute = name  # Private attribute
        self._protected_attribute = name  # Protected attribute
        self.public_attribute = name  # Public attribute

    def get_private_attribute(self):
        return self.__private_attribute
    
    def set_private_attribute(self, value):
        self.__private_attribute = value
 
    # Other methods...

# Create an instance of the class

# obj = ClassName('Ahmed')
# print(obj.public_attribute)
# print(obj.__private_attribute)
# print(obj.get_private_attribute())
# obj = ClassName('arsalan')
# print(obj.get_private_attribute())
# obj.set_private_attribute(42)
# print(obj.get_private_attribute())






# Public Attributes: These attributes are accessible from anywhere, both within the class and from outside the class. They can be accessed directly using the object of the class.

# Private Attributes: These attributes are only accessible within the class in which they are defined. They are denoted by adding a double underscore (__) prefix to the attribute name. Private attributes can only be accessed using methods defined within the class, known as getter and setter methods.

# Protected Attributes: These attributes are not truly private like private attributes, but they are intended to indicate that the attribute is for internal use within the class and its subclasses. They are denoted by adding a single underscore (_) prefix to the attribute name. Protected attributes are accessible within the class and its subclasses, but they can still be accessed directly.




# ----------------------------- Question -------------------------------

# Define a class called "Student" with private attributes "name", "age", and "roll_number". Implement methods to set and get these attributes. Demonstrate encapsulation by accessing and modifying these attributes through the methods.

class Student:
    def __init__(self, name, age, newname) -> None:
        self.__name = name #private attribute
        self.__age = age #private attribute
        self.newname = newname #public attribute
    
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age

    def set_name(self, rename):
        self.__name = rename
    
    def set_age(self, newAge):
        self.__age = newAge
    

arsalan = Student('arsalan', 22, 'newArsalan')
print(arsalan.get_name())
print(arsalan.get_age())

# using the set methods

arsalan.set_name('arham')
print(arsalan.get_name())

arsalan.set_age(35)
print(arsalan.get_age())

# Trying to access the attributes directly without using the get or set method
print(arsalan.newname)
print()
print()
print()
print()
# print(arsalan.__name)
