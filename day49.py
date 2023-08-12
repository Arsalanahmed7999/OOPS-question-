# Hybrid Inheritance

# Create a class called "Device" with attributes "name" and "manufacturer". Implement a method called "display_info" that prints out the name and manufacturer of the device.

# Create a child class called "Computer" that inherits from the "Device" class. Add an additional attribute "cpu" to the "Computer" class. Implement a method called "display_specs" that calls the "display_info" method and prints out the CPU specifications.

# Create a child class called "Phone" that also inherits from the "Device" class. Add an additional attribute "os" to the "Phone" class. Implement a method called "display_info" that prints out the device name, manufacturer, and operating system.

# Create a grandchild class called "Smartphone" that inherits from both the "Computer" and "Phone" classes. Add an additional attribute "camera_resolution" to the "Smartphone" class. Implement a method called "display_details" that calls the "display_specs" method from the "Computer" class and prints out the camera resolution and OS from the "Phone" class.

# Parent Class

class Device:
    def __init__(self, name, manufacturer) -> None:
        self.name = name
        self.manufacturer = manufacturer
    
    def display_info(self):
        print(f'Name: {self.name}')
        print(f'Manufacturer: {self.manufacturer}')

# Child class - computer

class Computer(Device):
    def __init__(self, name, manufacturer, cpu) -> None:
        Device.__init__(self, name, manufacturer)
        self.cpu = cpu
    
    def display_specs(self):
        self.display_info()
        print(f'CPU Specifications: {self.cpu}')

# Child class - Phone

class Phone(Device):
    def __init__(self, name, manufacturer, os) -> None:
        Device.__init__(self, name, manufacturer)
        self.os = os
    
    def display_info_c(self):
        self.display_info()
        print(f"Operating System: {self.os}")

# Grandchild - Smartphone

class Smartphone(Computer, Phone):
    def __init__(self, name, manufacturer, cpu, os, camera_resolution) -> None:
        Computer.__init__(self, name, manufacturer, cpu) 
        Phone.__init__(self, name, manufacturer, os)
        self.camera_resolution = camera_resolution
    
    def display_details(self):
        self.display_specs()
        print(f"Operating System: {self.os}")
        print(f'Camera Resoluton: {self.camera_resolution}')

# Create an instance - Devive 

a = Device("Name A ", 'Manufacturer A')
a.display_info()

print()
print()
print()
# Creating an instance - Computer

b = Computer('Name B', 'Manufacturer B ', 'Cpu Specification for B')
b.display_specs()


print()
print()
print()
# Creating an instance - Phone

c = Phone('Name C', "Manufacturer C", "Windows OS")
c.display_info_c()

# Grandchild Class Smartphone
print()
print()
print()
d = Smartphone('Name D', 'Manufacturer D', 'Cpu Specification for D ', 'Android', '32 megapixels')
d.display_details()