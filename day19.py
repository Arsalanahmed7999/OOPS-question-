#1 Create a class called "Animal" with attributes "name" and "sound". Create a child class called "Cat" that inherits from the "Animal" class. Override the "sound" attribute in the "Cat" class to make it "meow". Create an instance of the "Cat" class and print out the name and sound of the cat.

class Animal:
    def __init__(self, name, sound) -> None:
        self.name = name
        self.sound = sound

class Cat(Animal):
    # def __init__(self, name) -> None:
    #     super().__init__(name, 'Meow')
    def __init__(self, name) -> None:
        super().__init__(name, 'Meow')



Dog = Animal('tommy', 'bark')
# print(Dog.sound)
a = Cat('kitty')
print(f'The name of cat is: {a.name}')
print(f'The sound of cat is: {a.sound}')
