# --------------------- Polymorphism --------------------------


# Polymorphism is a fundamental concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It enables the same method name to be used for different classes, and the appropriate method is called based on the object's actual type or class. Polymorphism helps achieve code reusability, flexibility, and a more organized code structure.

# Polymorphism is often achieved through method overriding, where a subclass provides a specific implementation for a method that is already defined in its superclass. This allows different subclasses to have different behaviors for the same method.



# -----------------------------Basic Structure --------------------------


# class Animal:
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         return "Woof!"

# class Cat(Animal):
#     def make_sound(self):
#         return "Meow!"

# # Creating instances of Dog and Cat
# dog = Dog()
# cat = Cat()

# # Calling the make_sound method on different animal objects
# print(dog.make_sound())
# print(cat.make_sound())

# ------------------------ Question --------------------------------------
# Explain the concept of polymorphism in object-oriented programming. Provide an example to illustrate how polymorphism works.


# Parent Class

class Animal:
    def display_sound(self):
        return 'sound of an animal'


# Child Class - Dog

class Dog(Animal):
    def display_sound(self):
        return "Woof!"

# Child Class - Cat

class Cat(Animal):
    def display_sound(self):
        return "Meow!"
    
# Child Class - Cow

class Cow(Animal):
    def display_sound(self):
        return "Moo!"

dog = Dog()
cat = Cat()
cow = Cow()
# print(a.display_sound())
# print(b.display_sound())
# print(c.display_sound())

animals = [dog, cat, cow]


for animal in animals: #[dog, cat, cow]
    print(animal.display_sound())

