#1 Create three parent classes, "Food", "Vegetarian", and "Vegan", each with specific attributes and methods related to their dietary characteristics.

# Create a child class called "VeganVegetarianFood" that inherits from both "Vegetarian" and "Vegan". Implement a method called "consume" in the "VeganVegetarianFood" class that calls the methods from both parent classes to demonstrate vegetarian and vegan dietary choices.

# Create an instance of the "VeganVegetarianFood" class and call the "consume" method to demonstrate the dietary characteristics inherited from both parent classes.

# Parent 1
class Food:
    def __init__(self, name) -> None:
        self.name = name
    
    def eat(self):
        print('Eating food')
    

# Parent 2

class Vegetarian:
    def vegetarian_diet(self):
        print('Following vegetarian diet')

# Parent 3

class Vegan:
    def vegan_diet(self):
        print('Following vegan diet')

# Child class

class VeganVegetarianFood(Vegetarian, Vegan):
    def consume_vegetarian(self):
        self.vegetarian_diet()
    def consume_vegan(self):
            self.vegan_diet()

# Creating an object for VeganVegetarianFood
a = VeganVegetarianFood()
a.consume_vegetarian()
a.consume_vegan()

# Creating an object for vegetarian
b = Vegetarian()
b.vegetarian_diet()