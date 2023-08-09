# Multilevel inheritance Question

# Create a class called "Product" with attributes "name" and "price". Implement a method called "display_info" that prints out the name and price of the product.

# Create a child class called "Electronics" that inherits from the "Product" class. Add an additional attribute called "brand" to represent the brand of the electronic product. Implement a method called "display_brand" that prints out the brand of the electronic product.

# Create a grandchild class called "Smartphone" that inherits from the "Electronics" class. Add an additional attribute called "screen_size" to represent the screen size of the smartphone. Implement a method called "display_screen_size" that prints out the screen size of the smartphone.

# Create an instance of the "Smartphone" class with specific values for the name, price, brand, and screen size. Call the "display_info" method to print out the name and price of the smartphone. Then, call the "display_brand" method to print out the brand. Finally, call the "display_screen_size" method to print out the screen size of the smartphone.

# Parent class

class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
    
    def display_info(self):
        print(f'Name: {self.name}\nPrice: {self.price}')

# Child Class 1

class Electronics(Product):
    def __init__(self, name, price, brand) -> None:
        super().__init__(name, price)
        self.brand = brand
    
    def display_brand(self):
        print(f"Brand: {self.brand}")

# Child Class 2

class Smartphone(Electronics):
    def __init__(self, name, price, brand, screen_size) -> None:
        super().__init__(name, price, brand)
        self.screen_size = screen_size
    
    def display_screen_size(self):
        print(f"Screen Size: {self.screen_size}")


# Creating an instance 

samsumg = Smartphone('s7', 15000, "Samsung", '10inch x 7inch')

samsumg.display_info()
samsumg.display_brand()
samsumg.display_screen_size()

# a = Product('salt', 15)
# a.display_info()