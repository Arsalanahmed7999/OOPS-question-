#1 Create three parent classes, "Device", "Smart", and "Portable", each with specific attributes and methods related to their functionalities.

# Create a child class called "SmartPortableDevice" that inherits from both "Smart" and "Portable". Implement a method called "use" in the "SmartPortableDevice" class that calls the methods from both parent classes to demonstrate smart.

# Parent 1

class Device:
    def __init__(self, name) -> None:
        self.name = name
    
    def turn_on(self):
        print(f'The device {self.name} is turning on')

    def turn_off(self):
        print(f'The device {self.name} is turning off')

# Parent 2

class Smart:
    def connet_to_internet(self):
        print('Connecting to internet')


# Parent 3

class Portable:
    def carry_device(self):
        print('Carrying the device')


# Child Class

# class SmartPortableDevice(Smart, Portable):
#     def use(self):
#         self.connet_to_internet()
#         self.carry_device()

class SmartPortableDevice(Device, Smart, Portable):
    def use(self):
        self.connet_to_internet()
        self.carry_device()

iPhone = SmartPortableDevice('iphone 7 plus') 
iPhone.use()

