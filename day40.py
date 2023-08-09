# Heirarchical Inheritance

# Create a class called "Vehicle" with attributes "manufacturer" and "model". Implement a method called "display_info" that prints out the manufacturer and model of the vehicle.

# Create two child classes, "Car" and "Motorcycle", both inheriting from the "Vehicle" class. Add an additional attribute "num_doors" to the "Car" class and "num_wheels" to the "Motorcycle" class.

# Create instances of both child classes and set specific values for the "manufacturer", "model", "num_doors", and "num_wheels" attributes. Call the "display_info" method for each instance to print out the manufacturer and model of the vehicle.

# Parent Class

class Vehicle:
    def __init__(self, manufacturer, model) -> None:
        self.manufacturer = manufacturer
        self.model = model
    
    def display_info(self):
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Model: {self.model}")

# Child Class 
class Car(Vehicle):
    def __init__(self, manufacturer, model, num_doors) -> None:
        super().__init__(manufacturer, model)
        self.num_doors = num_doors

# Child Class 
class Motorcycle(Vehicle):
    def __init__(self, manufacturer, model, num_wheels) -> None:
        super().__init__(manufacturer, model)
        self.num_wheels = num_wheels

# Instance for Car
Tata = Car('Tata', 'Nano', 4)
Tata.display_info()
print(Tata.num_doors)

# Instance for Motorcycle
splendor = Motorcycle('Hero', 'splendor', 2)
splendor.display_info()
print(splendor.num_wheels)