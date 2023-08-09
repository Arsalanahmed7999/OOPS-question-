# HYBRID INHERITANCE

# ---------------------- QUESTION -----------------------------

# Create a base class called Vehicle. The Vehicle class should have a method called display_info() that prints "This is a vehicle."

# Create two derived classes called Car and Bicycle.

# The Car class should inherit from Vehicle and have additional attributes make and model. Implement the display_info() method in the Car class to display the make and model information of the car.

# The Bicycle class should also inherit from Vehicle and have an additional attribute brand. Implement the display_info() method in the Bicycle class to display the brand information of the bicycle.

# Finally, create a Hybrid class that inherits from both Car and Bicycle. The Hybrid class should have an additional attribute electric_mode. Implement the display_info() method in the Hybrid class to display the make, model, brand, and electric mode information of the hybrid vehicle.

# Parent Class 

class Vehicle:
    def display_info(self):
        print('This is a Vehicle')

# Child Class 1 

class Car(Vehicle):
    def __init__(self, make, model) -> None:
        self.make = make 
        self.model = model
    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")


# Child Class 2

class Bicycle(Vehicle):
    def __init__(self, brand) -> None:
        self.brand =  brand
    
    def display_info(self):
        print(f"Brand: {self.brand}")

class Hybrid(Car, Bicycle):
    def __init__(self, make, model, brand, electric_mode) -> None:
        Car.__init__(self, make, model)
        Bicycle.__init__(self, brand)
        self.electric_mode = electric_mode
    
    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Brand: {self.brand}")
        print(f"Electic Mode : {self.electric_mode}")

a = Hybrid('make', 'model', 'tata', True)
a.display_info()

# QUICK QUIZ - What type of inheritance is this where there is a single parent class and it has multiple child class ?

