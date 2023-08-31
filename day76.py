# --------------------- Abstraction -----------------------------



# --------------------- Question --------------------------------

# Create an abstract class called "Product" with an abstract method "calculate_total_price". Implement two subclasses, "Book" and "Electronics", that inherit from "Product" and provide their own implementations for calculating total price.

# Parent class 
from abc import ABC, abstractmethod
class Product(ABC): #concrete class to abstract

    def __init__(self, name, quatity, price) -> None:
        self.name = name
        self.price = price
        self.quantity = quatity

    @abstractmethod
    def calculate_total_price(self): #concrete method to abstract method
        pass

# child class book

class Book(Product):
    def __init__(self, name, quatity, price, tax) -> None:
        super().__init__(name, quatity, price)
        self.tax = tax

    def calculate_total_price(self):
        total_price = self.quantity * self.price * (self.tax / 100)
        return total_price
    



class Electronics(Product):
    def __init__(self, name, quatity, price, warranty_fee) -> None:
        super().__init__(name, quatity, price)
        self.warranty_fee = warranty_fee
    def calculate_total_price(self):
        total_price = self.quantity * self.price * self.warranty_fee
        return total_price


# shoes = Product() # we cannot instantiate for our abstract class
# shoes.calculate_total_price()

book = Book('kite runner', 5, 100, 5)
print(book.calculate_total_price())

electronic = Electronics('ear phones', 10, 200, 50)
print(electronic.calculate_total_price())