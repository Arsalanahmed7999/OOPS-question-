# ------------------------- QUESTION ---------------------------
# HYBRID INHERITANCE

# Create a class called "Animal" with attributes "species" and "sound". Implement a method called "make_sound" that prints out the sound of the animal.

# Create two child classes called "Bird" and "Mammal", both inheriting from the "Animal" class.

# For the "Bird" class, add an additional attribute "wing_span" to represent the wingspan of the bird. Implement a method called "fly" that prints out a message indicating that the bird is flying.

# For the "Mammal" class, add an additional attribute "num_legs" to represent the number of legs of the mammal. Implement a method called "walk" that prints out a message indicating that the mammal is walking.

# Create a grandchild class called "Bat" that inherits from both the "Bird" and "Mammal" classes.

# For the "Bat" class, add an additional attribute "echolocation" to represent whether the bat uses echolocation or not. Implement a method called "display_info" that calls the "make_sound" method from the "Animal" class to print out the sound of the bat, and also prints out the wingspan, number of legs, and echolocation ability of the bat.

# Create an instance of the "Bat" class with specific values for the species, sound, wing span, number of legs, and echolocation. Call the "display_info" method to print out the information of the bat.


# Parent Class
class Animal:
    def __init__(self, species, sound) -> None:
        self.species = species
        self.sound = sound
    def display_sound(self):
        print(f"The sound of the {self.species} is {self.sound}")

# Child Class Bird

class Bird(Animal):
    def __init__(self, species, sound, wing_span) -> None:
        Animal.__init__(self, species, sound)
        self.wing_span = wing_span
    def fly(self):
        print(f"The bird in Flying")

# Child Class Mammal

class Mammal(Animal):
    def __init__(self, species, sound, num_legs) -> None:
        Animal.__init__(self, species, sound)
        self.num_legs = num_legs

    def walking(self):
        print('The Mammal is walking')


# Grandchild Bat - Parent Class (Bird, Mammal)

class Bat(Bird, Mammal):
    def __init__(self, species, num_legs, sound, wing_span, echolocation) -> None:
        Bird.__init__(self, species, sound, wing_span)
        Mammal.__init__(self, species, sound, num_legs)
        self.echolocation = echolocation
    def display_info(self):
        self.display_sound()
        self.fly()
        self.walking()
        print(f"Echolocation: {self.echolocation}")

xyz = Bat('xspecies', 2 , 'xsound', '20cm', True)
xyz.display_info()