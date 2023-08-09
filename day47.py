# ------------------------- QUESTION ---------------------------
# HYBRID INHERITANCE

# Create a class called "Vehicle" with an attribute "color". Implement a method called "display_color" that prints out the color of the vehicle.

# Create two child classes called "Car" and "Motorcycle", both inheriting from the "Vehicle" class.

# For the "Car" class, add an additional attribute "num_doors" to represent the number of doors of the car. Implement a method called "display_doors" that prints out the number of doors.

# For the "Motorcycle" class, add an additional attribute "num_wheels" to represent the number of wheels of the motorcycle. Implement a method called "display_wheels" that prints out the number of wheels.

# Create a grandchild class called "HybridCar" that inherits from both the "Car" and "Motorcycle" classes.

# For the "HybridCar" class, add an additional attribute "fuel_type" to represent the fuel type of the hybrid car. Implement a method called "display_fuel_type" that prints out the fuel type.

# Create instances of the "Car", "Motorcycle", and "HybridCar" classes with specific values for the attributes. Call the respective methods to display the color, number of doors, number of wheels, and fuel type of the hybrid car.

# Parent Class
class Vehicle:
    def __init__(self, color) -> None:
        self.color = color
    
    def display_color(self):
        print(f"Color: {self.color}")

# Child Class

class Car(Vehicle):
    def __init__(self, color, num_doors) -> None:
        super().__init__(color)
        self.num_doors = num_doors
    def display_doors(self):
        print(f"Number of Doors: {self.num_doors}")

# Child Class

class Motorcycle(Vehicle):
    def __init__(self, color, num_wheels) -> None:
        super().__init__(color)
        self.num_wheels = num_wheels
    
    def display_wheels(self):
        print(f"Number of Wheels: {self.num_wheels}")
    
# Grandchild HybridCar - (Parent class of hybridcar - Car, Motorcycle)

class HybridCar(Car, MemoryError):
    def __init__(self, color, num_doors, fuel_type) -> None:
        super().__init__(color, num_doors)
        self.fuel_type = fuel_type
    
    def display_fuel_type(self):
        print(f"Fuel Type: {self.fuel_type}")


# Create an instance for Car

acar = Car('red', 5)
acar.display_doors()

# Create an instance for Motorcycle

xmotorcylce = Motorcycle('black', 2)
xmotorcylce.display_wheels()
# Create an instance for Hybridcard

xyz = HybridCar('blue', 4, 'Petrol')
xyz.display_fuel_type()