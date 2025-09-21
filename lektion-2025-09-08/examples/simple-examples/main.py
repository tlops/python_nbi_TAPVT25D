def add(a, b):
    return a + b

class BankAccount:
    def __init__(self, owner, saldo=0):
        self.owner = owner
        self.saldo = saldo

    def deposit(self, amount):
        self.saldo += amount

    def withdraw(self, amount):
        if amount <= self.saldo:
            self.saldo -= amount
            return True
        return False

def divide():
    number = int(input("Skriv in ett tal: "))

    if number == 0:
        raise ZeroDivisionError("Du kan inte dela med noll")
    
    result = 10 / number
    return result