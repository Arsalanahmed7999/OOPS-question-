# --------------------- Abstraction -----------------------------



# --------------------- Question ----------------------------

# Create an abstract class called "Animal" with an abstract method "make_sound". Create two subclasses "Dog" and "Cat" that inherit from "Animal" and provide their own implementations for "make_sound".
# How does Python's abc module contribute to abstraction? Give an example of using the ABC class.

from abc import ABC, abstractmethod

# Parent Class
class Animal(ABC): #abstract class 
    # we have to make this an abstraction method
    @abstractmethod
    def make_sound(self):
        pass

# Child Class Dog

class Dog(Animal): #concrete class
    # This is a needed method to run the code 
    def make_sound(self):
        print('The sound of the animal is WOOF!')

    def walk(self):
        print('The animal is walking')

# Child Class Cat

class Cat(Animal): #concrete class
    # This is a needed method to run the code 
    def make_sound(self):
        print('The sound of the animal is MOEW!')
    def walk(self):
        print('The animal is walking')

dog = Dog()
dog.make_sound()
cat = Cat()
cat.make_sound()