# -------------------- Encapsulation ---------------------

#  ---------------------------- Question --------------------------

# Create a class called "BankAccount" with private attributes "account_number" and "balance". Implement methods to deposit and withdraw funds, taking into account encapsulation principles. Demonstrate the use of these methods.

class BankAccount:
    def __init__(self, account_number, balance) -> None:
        self.__account_number = account_number #private 
        self.__balance = balance #private
    
    def deposit(self, amount):
        self.__balance+=amount
    
    def withdraw(self, amount):
        if((self.__balance - amount) > 0):
            self.__balance-=amount
            print(f'Withdrawal of {amount} has been successful from account number {self.__account_number}')
        else:
            print ('Insufficient Balance')
    
    def info(self):
        return f"Account Number : {self.__account_number}\nBalance : {self.__balance}"
        
axis = BankAccount(50678902312, 100000)
# print(axis.__balance)
# print(axis.__account_number)
# print(axis.info())


# Lets apply it on our deposit and withdraw methods

sbi = BankAccount(190002134, 10000)
print(sbi.info())
sbi.deposit(2000)
print(sbi.info())
sbi.withdraw(4000)
print(sbi.info())
print()
print()
print()
sbi.withdraw(9000)
print(sbi.info())
