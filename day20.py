#1. Create a class called "Bird" that inherits from the "Animal" class. Add an additional instance attribute called "species" specific to the Bird class. Implement a method called "speak" that prints out a bird-specific message like "The bird chirps melodiously." Create an instance of the Bird class and call the "speak" method.

class Animal:
    def __init__(self, name, sound) -> None:
        self.name = name
        self.sound = sound

class Bird(Animal):
    def __init__(self, name, sound, species) -> None:
        super().__init__(name, sound) #super means that these attributes belond to the parent class (Animal).
        self.species = species
    
    def speak(self):
        return "The bird chirps melodiously."

a = Bird('pico', 'chirps', 'Sparrow')
print(f"The name is: {a.name}")
print(f"The sound of bird is: {a.sound}")
print(f"The Species of the Bird is: {a.species}")
print(a.speak())
