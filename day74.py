# --------------------- Abstraction -----------------------------



# --------------------- Question --------------------------------

# Create an abstract class called "Vehicle" with abstract methods "start_engine" and "stop_engine". Implement two subclasses, "Car" and "Motorcycle", that inherit from "Vehicle" and provide their own implementations for starting and stopping the engine.

# Parent Class 
from abc import ABC, abstractmethod
class Vehicle(ABC): #concrete class has been changed to abstract class 
    @abstractmethod
    def start_engine(self): #concrete method has been changed to abstract method
        pass
    @abstractmethod
    def stop_engine(self): #concrete method has been changed to abstract method
        pass

# Child class car

class Car(Vehicle):
    def info(self):
        print('This is a car')

    def start_engine(self):
        print("Car's engine is starting")
    
    def stop_engine(self):
        print("Car's engine is stoping")

# Child class motorcycle  
class Motorcycle(Vehicle):
    def info(self):
        print('This is a motorcycle')

    def start_engine(self):
        print("Motorcycle's engine is starting")
    
    def stop_engine(self):
        print("Motorcycle's engine is stoping")

# a = Vehicle() #we cannot create an instance for our abstract class 
car = Car()
car.info()

motorcycle = Motorcycle()
motorcycle.info()