#1 Create a class called "BankAccount" with attributes "account_number" and "balance". Create a child class called "SavingsAccount" that inherits from the "BankAccount" class. Add an attribute called "interest_rate" to the "SavingsAccount" class. Implement a method in the "SavingsAccount" class that calculates and returns the interest earned on the balance. Create an instance of the "SavingsAccount" class and test the method.

class BankAccount:
    def __init__(self, account_number, balance) -> None:
        self.account_number = account_number
        self.balance = balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate) -> None:
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    
    def calculate_interest(self):
        #interest_amount = 0.05 * 1000 = 50
        interest_amount = self.interest_rate * self.balance
        #self.balance = 1000 + 50 = 1050
        self.balance = self.balance + interest_amount

a = SavingsAccount(50334432311231, 1000, 0.05)
#initial balance 
print(a.balance)    
#after running the calculate_interest method
a.calculate_interest()
print(a.balance)

#after running the calculate_interest method
# now it be calculating interest amount on 1050 not on 1000
# so it will be interest_amount = 0.05 * 1050
# balance = interest_amount(0.05 * 1050) + 1050
a.calculate_interest()
print(a.balance)

a.calculate_interest()
print(a.balance)




