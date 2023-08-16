# --------------------- Polymorphism --------------------------


# ---------------------- Question -----------------------------

# Create a class hierarchy with a base class "Vehicle" and subclasses "Car", "Bicycle", and "Motorcycle". Implement a method called "describe" in each class. Demonstrate polymorphism by creating a dictionary with keys as vehicle names and values as instances of different vehicle classes. Iterate through the dictionary and call the "describe" method on each object.

# Parent - Vehicle
class Vehicle:
    def describe(self):
        return "This is a Vehicle"

# Child Class - Car
class Car(Vehicle):
    def describe(self):
        return 'This is a Car'
    
# Child Class - Bicycle
class Bicycle(Vehicle):
    def describe(self):
        return 'This is a Bicycle'
    
# Child Class -Motorcycle
class Motorcycle(Vehicle):
    def describe(self):
        return 'This is a Motorcycle'


# creating instances of each individual classes

car_instance = Car()
bicycle_instance = Bicycle()
motorcycle_instance = Motorcycle()


vehicles = {
    # key (name of the vehicle) : value(instance of the vehicle)
    'car': car_instance,
    'bicycle': bicycle_instance,
    'motorcycle' : motorcycle_instance
}

for key, value in vehicles.items():
    # value is the instance
    description = value.describe()
    print(f"{key}: {description}")