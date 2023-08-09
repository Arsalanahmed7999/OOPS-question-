#1 Create two parent classes, "Animal" and "Pet", with attributes and methods specific to each class, such as "make_sound" in "Animal" and "play" in "Pet".

# Create a child class called "Dog" that inherits from both "Animal" and "Pet". Implement a method called "interact" in the "Dog" class that calls the methods from both parent classes to make a sound and play. Create an instance of the "Dog" class and call the "interact" method.

# Parent Class 1

class Animal:
    def make_sound(self):
        return 'Animal is making sound'


# Parent Class 2

class Pet:
    def play(self):
        return "The animal is playing" 

# Child Class

class Dog(Animal, Pet):
    def interact(self):
        sound = self.make_sound()
        play = self.play()
        return sound, play

# Creating an instance here

dog = Dog()
print(dog.interact())