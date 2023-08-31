# --------------------- Abstraction -----------------------------



# --------------------- Question --------------------------------

# Create an abstract class called "BankAccount" with abstract methods "deposit" and "withdraw". Implement two subclasses, "SavingsAccount" and "CheckingAccount", that inherit from "BankAccount" and provide their own implementations for depositing and withdrawing money.

# parent class 
from abc import ABC, abstractmethod
class BankAccount(ABC): #Concrete class has been changed to abstract class

    @abstractmethod 
    def deposit(self): #concrete method has been changed to abstract method
        pass
    @abstractmethod
    def withdraw(self): #concrete method has been changed to abstract method
        pass


# child class savingsaccount

class SavingsAccount(BankAccount): #concrete class
    def __init__(self, balance) -> None:
        super().__init__()
        self.balance = balance 

    def deposit(self, amount):
        self.balance+=amount
        
    def withdraw(self, amount):
        # i have to take out the money from the bankaccount
        # I have to check that the amount i want to withdraw should be less than the balance in bankaccount 
        if(self.balance - amount >= 0):
            self.balance-=amount
        else:
            print('You have insufficient balance and you cannot withdraw this amount')
    
    def info(self):
        print('This is my savings account', f'My balance: {self.balance}')

# child class CheckingAccount
class CheckingAccount(BankAccount):
    def __init__(self, balance) -> None:
        self.balance = balance
    
    def deposit(self, amount):
        self.balance+=amount
    
    def withdraw(self, amount):
        # i have to take out the money from the bankaccount
        # I have to also put a fees - 10
        # I have to check that the amount i want to withdraw should be less than the balance in bankaccount 
        fees = 10
        if(self.balance - (amount + fees) >= 0):
            self.balance-=(amount+fees)
        else:
            print('You have insufficient balance and you cannot withdraw this amount')


    def info(self):
        print('This is my checking account', f'My balance: {self.balance}')




# a = BankAccount() #this is an instance of my BankAccount (we cannot create this instance of abstract class)

savingaccount = SavingsAccount(1000) #concrete instance 
savingaccount.info() #we cannot instantiate without creating the abstract methods
savingaccount.deposit(500)
savingaccount.info()
savingaccount.withdraw(1200)
savingaccount.info()
savingaccount.withdraw(1200)
savingaccount.info()


# checking account instance
print()
print()
print('This is a checking account info')
chkacc = CheckingAccount(100)
chkacc.info()
chkacc.deposit(1000)
chkacc.info()
chkacc.withdraw(500)
chkacc.info()
chkacc.withdraw(1000)
chkacc.info()
chkacc.withdraw(580)
chkacc.info()

