#!/usr/bin/python3
# This program simulates a simple bank account with a menu-driven interface.
# It demonstrates object-oriented programming with a BankAccount class and error handling.

class Bank_Account:
    """
    A class to represent a simple bank account.
    """
    def __init__(self, initial_balance=0):
        # Set initial balance to 0
        self.balance = initial_balance

    def get_balance(self):
        # return current balance
        return self.balance

    def deposit(self, amount):
        # Deposit Money into the account
        # raise value error if amount is 0 or invalid charater
        if amount <= 0:
            raise ValueError("Error: You cannot deposit a negative or zero amount.")
        self.balance += amount
        print(f"You have successfully deposited {amount:.2f} Kr and your current balance is {self.balance}.")

    def withdrawal(self, amount): 
        # Withdraws money from the account.
        # raise value error if amount is 0 or invalid charater
        if amount > self.balance:
            raise ValueError(f"Error: Insufficient funds! You cannot withdraw more than current balance: {self.balance} Kr.")
        self.balance -= amount
        print(f"Successfully withdrew {amount:.2f} kr.")
        print(f"Your Current account balance is {self.balance} Kr.")
