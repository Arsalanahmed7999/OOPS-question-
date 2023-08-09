#1 Create three parent classes, "Vehicle", "Electric", and "Autonomous", each with specific attributes and methods related to their respective functionalities.

# Create a child class called "ElectricAutonomousVehicle" that inherits from both "Electric" and "Autonomous". Implement a method called "drive" in the "ElectricAutonomousVehicle" class that calls the methods from both parent classes to perform electric driving and autonomous driving functionalities.

# Create an instance of the "ElectricAutonomousVehicle" class and call the "drive" method to demonstrate the combined functionalities inherited from both parent classes.

# Parent 1
class Vehicle:
    def __init__(self, make, model) -> None:
        self.make = make
        self.model = model
    
    def start(self):
        print('The vehicle is starting')

# Parent 2
class Electric:
    def charge(self):
        print('The vehicle is charging')
    def drive_electric(self):
        print('The vehicle is driving electrically')

# Parent 3

class Autonomous:
    def navigate(self):
        print('The vehiclie navigates')
    def drive_autonomous(self):
        print('The vehicle drives autonomous')

# Child class

class ElectricAutonomousVehicle(Electric, Autonomous):
    def drive(self):
        self.drive_electric()
        self.drive_autonomous()

# Creating an object

tesla = ElectricAutonomousVehicle()
tesla.drive()
