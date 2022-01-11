class Account:

    # constructor
    def __init__(self, filepath):
        # instance variable
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance= self.balance - amount

    def deposit(self, amount):
        self.balance= self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):
    # Doc strings
    """This class generates checking account objects"""
    
    # class variable
    type="Checking"

    # constructor
    def __init__(self, filepath): 
        Account.__init__(self, filepath)


john_checking=Checking("john_balance.txt") # object instance
john_checking.deposit(100)
john_checking.commit()
print(john_checking.type)
print(john_checking.balance)


bob_checking=Checking("bob_balance.txt") # object instance
bob_checking.deposit(100)
bob_checking.commit()
print(bob_checking.type)
print(bob_checking.balance)

# print Doc strings
print(john_checking.__doc__)