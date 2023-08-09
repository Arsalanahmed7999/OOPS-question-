# Heirarchical Inheritance

# Create a class called "Animal" with attributes "species" and "sound". Implement a method called "make_sound" that prints out the sound of the animal.

# Create three child classes called "Cat", "Dog", and "Lion", each inheriting from the "Animal" class. Add an additional attribute specific to each child class, such as "breed" for the "Dog" class and "mane_color" for the "Lion" class. Implement methods for each child class to display their specific attributes.

# Create instances of the "Cat", "Dog", and "Lion" classes with specific values for the species, sound, and the additional attributes. Call the "make_sound" method for each instance to print out their sound.

# Parent Class

class Animal:
    def __init__(self, species, sound) -> None:
        self.species = species
        self.sound = sound
    def make_sound(self):
        print(f'The sound of the {self.species} is {self.sound}')

# Child Class
class Cat(Animal):
    def __init__(self, species, sound, breed) -> None:
        super().__init__(species, sound)
        self.breed = breed
    
    def display_cat_breed(self):
        print(f"Breed: {self.breed}")


# Child Class

class Dog(Animal):
    def __init__(self, species, sound, breed) -> None:
        super().__init__(species, sound)
        self.breed = breed
    
    def display_dog_breed(self):
        print(f"Breed: {self.breed}")

# Child Class

class Lion(Animal):
    def __init__(self, species, sound, mane_color) -> None:
        super().__init__(species, sound)
        self.mane_color = mane_color
    
    def display_mane_color(self):
        print(f"Mane Color: {self.mane_color}")

# Instance for Cat

a = Cat('xspecies', 'meow', 'xbreed')
a.make_sound()

# Instance for Dog

b = Dog('yspecies', 'bark', 'ybreed')
b.make_sound()
# Instance for Lion

c = Lion('zspecies', 'roar', 'zcolor')
c.make_sound()
c.display_mane_color()