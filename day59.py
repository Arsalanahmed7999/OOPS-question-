# --------------------- Polymorphism --------------------------

# ---------------------- Question -----------------------------

# Create a class called "Animal" with a method called "speak". Create subclasses "Dog", "Cat", and "Bird", and override the "speak" method in each subclass. Demonstrate polymorphism by creating a dictionary with animal names as keys and instances of different animal classes as values. Iterate through the dictionary and call the "speak" method on each object.

# Parent Class 
class Animal:
    def speak(self):
        pass #This method we will be overriding

# Child Class - Dog

class Dog(Animal):
    def speak(self):
        return 'Woof!' #Sound of a Dog

# Child Class - Cat

class Cat(Animal):
    def speak(self):
        return 'Meow!'

# Child Class - Bird

class Bird(Animal):
    def speak(self):
        return 'Chirp!'

# Instances of the child class

dog_instance = Dog() 
cat_instance = Cat()
bird_instance = Bird()

# dictionary = {
#     key : value
# }



animalDict = {
    'dog': dog_instance,
    'cat': cat_instance,
    'bird': bird_instance
}

# print(animalDict['dog'].speak())
# print(animalDict['cat'].speak())
# print(animalDict['bird'].speak())

for animalName, animalInstance in animalDict.items():
    print(f"The sound of {animalName} : {animalInstance.speak()}")
