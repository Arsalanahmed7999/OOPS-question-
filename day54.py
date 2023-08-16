# --------------------- Polymorphism --------------------------


# ---------------------- Question -----------------------------

# Create a class called "BankAccount" with methods "deposit" and "withdraw". Create subclasses "SavingsAccount" and "CheckingAccount" that override the "withdraw" method to apply different rules. Demonstrate polymorphism by using a list of "BankAccount" objects and calling the "withdraw" method on each object.

# Parent Class
class BankAccount:
    def __init__(self, balance) -> None:
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount  

    def withdraw(self):
        pass #This has to be overridden

# Child class SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, balance) -> None:
        super().__init__(balance)
    
    def withdraw(self, amount):
        if(self.balance - amount > 0):
            self.balance -= amount
            print(f'Your withdrawal of {amount} is successful from savings account')
        else:
            print('You have insufficient Balance')

# Child class CheckingAccount

class CheckingAccount(BankAccount):
    def __init__(self, balance) -> None:
        super().__init__(balance)
    
    withdrawal_fee = 10 #This is a withdrawal which can be changed

    def withdraw(self, amount):
        withdrawal_fee = 10 #This is a withdrawal which can be changed
        if((self.balance - (amount + withdrawal_fee)) > 0):
            self.balance-=(amount + withdrawal_fee)
            print(f'Your withdrawal of {amount} is successful from checking account')
        else:
            print('You have insufficient Balance')

savingsaccount = SavingsAccount(1000)
checkingaccount = CheckingAccount(3000)

bank_account = [savingsaccount, checkingaccount]

# checking the balance in both the account
for account in bank_account:
    print(f"Current Balance: {account.balance}")

# withdrawal of 500
for account in bank_account:
    (account.withdraw(500))

# checking the balance in both the account
for account in bank_account:
    print(f"Current Balance: {account.balance}")



