#1 Create a class called "Bank" with class-level attribute "bank_count" that represents the total count of banks. The attribute should be initialized to 0 and incremented every time a new bank object is created.

# The Bank class should also have instance attributes for "name" and "location" to represent the name and location of each bank. Additionally, include an instance attribute for "branches" as a list to store the names of branches in the bank.

# Implement methods to add a new branch to a bank and remove an existing branch from a bank.

# Create three instances of the Bank class with different names and locations. Add multiple branches to each bank. After creating the instances and adding branches, print out the total count of banks using the class-level attribute. Then, for each bank, print out the bank name, location, and the list of branches it has.

class Bank:
    bank_count = 0
    def __init__(self, name, location) -> None:
        self.name = name
        self.location = location
        self.branches = []
        Bank.bank_count+=1
    
    def add_branch(self, new_branch):
        self.branches.append(new_branch)
    
    def remove_branch(self, branch_name):
        if branch_name in self.branches:
            self.branches.remove(branch_name)
        else:
            return(f'There is no branch as {branch_name} in our branches')


print(Bank.bank_count)
bank1 = Bank('abc', 'xyz')
print(bank1.bank_count)
bank2 = Bank('abc', 'xyz')
print(bank1.bank_count)
bank3 = Bank('abc', 'xyz')
print(bank1.bank_count)


print(bank1.branches)

bank1.add_branch('new1')

print(bank1.branches)

# bank2 into consideration
print(bank2.branches)
bank2.add_branch('bank2 new-branch')
print(bank2.branches)
bank2.add_branch('bank2 new-branch2')
print(bank2.branches)
bank2.remove_branch('bank2 new-branch2')
print(bank2.branches)


# bank3 into consideration
# print(bank3.remove_branch('new1'))
# print(bank3.branches)
