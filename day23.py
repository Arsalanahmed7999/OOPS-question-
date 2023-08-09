#1 Create a class called "Vehicle" with attributes "brand" and "model". Implement a method called "display_info" that prints out the brand and model of the vehicle. Create a child class called "Car" that inherits from the "Vehicle" class. Add an additional attribute called "features" to the "Car" class, which should be a list to store different features of the car.

# Implement methods in the "Car" class to add a feature to the list, remove a feature from the list, and display all the features of the car. The method to add a feature should take a parameter "feature" and append it to the list. The method to remove a feature should take a parameter "feature" and remove it from the list.

# Create an instance of the "Car" class with specific values for the brand, model, and initial features. Call the "display_info" method to print out the brand and model of the car. Then, add some features using the method to add a feature. Remove a feature using the method to remove a feature. Finally, call the method to display all the features of the car.

class Vehicle:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model
    def display_info(self):
        return (f'The brand of vehicle is {self.brand} and the model is {self.model}')
    
class Car(Vehicle):
    def __init__(self, brand, model) -> None:
        super().__init__(brand, model)
        self.features = []
    
    def add_feature(self, feature):
        self.features.append(feature)
    
    def remove_feature(self, feature):
        if feature in self.features:
            self.features.remove(feature)
        else:
            return(f'The {feature} is not inside the features list')
    
    def display_features(self):
        return self.features


Nano = Car('Tata', 'Nano')
print(Nano.features)

Nano.add_feature('Car Navigation')
# print(Nano.features)

Nano.add_feature('Huge types')
# print(Nano.features)

Nano.add_feature('Multiple Seats')
# print(Nano.features)

Nano.remove_feature('bluetooth connectivity')
# print(Nano.features)


#I want to remove bluetooth connectivity
# ['Car Navigation', 'Huge types', 'Multiple Seats'] 


Nano.display_features()