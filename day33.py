# Create a class called Vehicle with an attribute manufacturer. Implement a method called display_manufacturer that prints out the manufacturer of the vehicle.

# Create a child class called Car that inherits from the Vehicle class. Add an additional attribute model to the Car class. Implement a method called display_model that prints out the model of the car.

# Create a grandchild class called ElectricCar that inherits from the Car class. Add an additional attribute range to the ElectricCar class. Implement a method called display_range that prints out the range of the electric car.

# Create a great-grandchild class called Tesla that inherits from the ElectricCar class. Add an additional attribute autopilot to the Tesla class. Implement a method called display_info that prints out the manufacturer, model, range, and autopilot availability of the Tesla.

# Create an instance of the Tesla class with specific values for the manufacturer, model, range, and autopilot. Call the display_info method to print out the information of the Tesla.


# Parent class
class Vehicle:
    def __init__(self, manufacturer) -> None:
        self.manufacturer = manufacturer
    
    def display_manufacturer(self):
        return f"The Manufacturer: {self.manufacturer}"

# Child class 1

class Car(Vehicle):
    def __init__(self, manufacturer, model) -> None:
        super().__init__(manufacturer)
        self.model = model
    
    def display_model(self):
        return f"The model: {self.model}"

# Child Class 2

class ElectricCar(Car):
    def __init__(self, manufacturer, model, range) -> None:
        super().__init__(manufacturer, model)
        self.range = range
    
    def display_range(self):
        return f"The range: {self.range}"

# Child class 3 great-grandchild 

class Tesla(ElectricCar):
    def __init__(self, manufacturer, model, range, autopilot) -> None:
        super().__init__(manufacturer, model, range)
        self.autopilot = autopilot
    
    def display_info(self):
        return f"The Manufacturer: {self.manufacturer}\nThe model: {self.model}\nThe range: {self.range}\nThe autopilot availability: {self.autopilot}"

# An instance for great grand child - TESLA
a = Tesla('xyz', 'abc', '15', True)
print(a.display_info())
    