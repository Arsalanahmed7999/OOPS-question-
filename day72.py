# --------------------- Abstraction -----------------------------



# --------------------- Question ----------------------------

# Define an abstract class "Vehicle" with attributes "color" and "model". Create a concrete subclass "Car" that implements the abstract methods and attributes.

# Concrete v/s Abstract 
# Real, or it is not hidden v/s Hidden

from abc import ABC, abstractmethod
# Parent Class
class Vehicle(ABC): #so we have change this class from concrete to an abstract
    def __init__(self, color, model) -> None:
        self.model = model #public attribute
        self.color = color #public attribute
    @abstractmethod
    def info(self):
        pass

class Car(Vehicle): #concrete class 
    def __init__(self, color, model) -> None:
        super().__init__(color, model)
    
    def info(self):
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")

# parent object
# bike = Vehicle('blue', 'splendor')
# bike.info()

# child object
car = Car('Black', 'honda city')
car.info()

# we cannot create an instance for our abstract class 