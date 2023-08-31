# --------------------- Abstraction -----------------------------

# Imagine you're building a video game. In the game, you have different types of characters: warriors, wizards, and archers. Each character has properties like health, attack power, and special abilities.

# Now, let's think about abstraction in terms of this game:

# Real World vs. Abstraction: In the real world, each character has specific details and behaviors. But in the game's code, you don't need to represent every detail. You abstract away unnecessary specifics and focus only on the most important aspects of characters.

# Creating an Abstract Class: You create an abstract class called "Character." This class defines the common attributes and methods that every character should have, like health, attack(), and move(). However, you don't provide implementations for these methods in the abstract class because the way warriors attack or move might be different from wizards.

# Concrete Subclasses: You create concrete subclasses for each character type: Warrior, Wizard, and Archer. Each of these subclasses inherits from the Character abstract class. In these subclasses, you provide specific implementations for the methods like attack() and move().

# Using Abstraction: Now, in your game code, when you create instances of characters, you don't need to know all the nitty-gritty details about how each type of character attacks or moves. You just know that every character has these methods and attributes because of the abstract class. You can call character.attack() without caring whether it's a warrior, wizard, or archer.

# In this scenario, abstraction helps you focus on the core features and behaviors of characters without getting bogged down in the specific details of each type. It simplifies your code and allows you to work with a common interface (the methods defined in the abstract class) while hiding the individual implementations.

# To put it even more simply, abstraction is like using a TV remote. You don't need to know how pressing a button changes the channel – you just know that it does. The remote abstracts away the complicated inner workings of the TV. Similarly, abstract classes provide a way to work with objects without needing to understand all the internal complexities.

# ------------ Basic Understading / Basic ------------------
# from abc import ABC, abstractmethod
# class Developers(ABC): #abstract class
#     def database(self):
#         print('Connected to the database')

#     @abstractmethod
#     def security(self):
#         pass

# class webdeveloper(Developers): #concrete classes means they real and the are not hidden
    
# # to access the parent class Developers this child class has to pass a security check
#     def info(self):
#         print('This is a web developer')
    
#     def security(self):
#         print('Security check inside web developer class')

# class mobiledeveloper(Developers): #concrete classes means they real and the are not hidden
#     def mobile_info(self):
#         print('This is a mobile developer')
    
#     def security(self):
#         print('The security check for mobile developer')

# a = webdeveloper()
# a.info()
# a.database()

# b = mobiledeveloper()
# b.mobile_info()



# ------------------  Question ------------------------
# Define a class called "Shape" with an abstract method "calculate_area". What is the purpose of this abstract method?
# How can you create an abstract class in Python? Provide an example.
# Can you directly create an instance of an abstract class? Why or why not?
# Why do abstract methods have no implementation in the abstract class?
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod #abstract method
    def calculate_area(self):
        pass
    

a = Shape() #we cannot actually create an instance of our abstract class
print(a)

    

