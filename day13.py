#1. Create a class called "Vehicle" with class-level attribute "vehicle_count" that represents the total count of vehicles. The attribute should be initialized to 0 and incremented every time a new vehicle object is created.

# The Vehicle class should also have instance attributes for "make" and "model" to represent the make and model of each vehicle.

# Create three instances of the Vehicle class with different make and model values. After creating the instances, print out the total count of vehicles using the class-level attribute.

class Vehicle:
    vehicle_count = 0 #class level attribute
    def __init__(self, make, model) -> None:
        self.make = make
        self.model = model
        Vehicle.vehicle_count+=1

print(Vehicle.vehicle_count)
bike1 = Vehicle('honda', 'shine') #object1 , instance1
print(Vehicle.vehicle_count)
bike2 = Vehicle('honda', 'shine') #object2 , instance2
print(Vehicle.vehicle_count)
bike3 = Vehicle('honda', 'shine') #object3 , instance3
print(Vehicle.vehicle_count)

# Each time the vehicle is created which means that an object is created. Which means that the vehicle count should be incremented by 1. 