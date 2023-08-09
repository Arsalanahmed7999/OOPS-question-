#1. Create a class called "BankAccount" with attributes account_number, account_holder_name, and balance. Implement methods to deposit and withdraw money from the account. Create an instance of the class, perform some deposits and withdrawals, and print out the final balance.

class BackAccount:
    def __init__(self, account_number, account_holder_name, balance) -> None:
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance+=amount
    
    def withdraw(self, amount):
        if(self.balance > amount):
            self.balance-=amount
        else:
            print('Innsufficient balance')

Axis = BackAccount(1234567890, 'Any Nam', 3000)

print(Axis.balance)
Axis.deposit(1000)
print(Axis.balance)
Axis.withdraw(100)
print(Axis.balance)
Axis.withdraw(10000)
(Axis.balance)

#2. Create a class called "Product" with attributes name, price, and quantity. Implement a method to calculate and return the total cost of the product (price multiplied by quantity). Create an instance of the class with some sample values for price and quantity, and print out the total cost of the product.

class Product:
    def __init__(self, name, price, quantity) -> None:
        self.name = name 
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        totalcost = self.price * self.quantity
        # return self.price * self.quantity
        return f"Total cost = {totalcost}"
    
a = Product('salt', 100, 4)
print(a.total_cost())