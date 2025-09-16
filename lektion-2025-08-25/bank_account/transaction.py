#!/usr/bin/python3
from bank_class import Bank_Account

# The main program that provides a menu to the user for interacting with the bank account.


def display_menu():
    print("\n--- Display Menu ---")
    print("1. Deposit Cash")
    print("2. Withdraw Cash")
    print("3. Check Balance")
    print("4. Exit")

def main_menu():
    account = Bank_Account(100) # Start with an initial balance of 100 kr

    while True:
        # Display the menu options.
        display_menu()
        try: 
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("ERROR: You can only enter values 1-4 !")
            continue # Returns back to main menu. 
        
        if choice == 1:
            # Handle deposit option
            print("Deposit Cash: \n")
            try: 
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError as e:
                print(f"ERROR: {e}. Please enter a valid positive number.")

        elif choice == 2:
            # Handle withdrawal option.
            print("Withdraw Cash: ")
            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdrawal(amount)
            except ValueError as e:
                print(f"ERROR: {e}. Please enter a valid positive number.")

        elif choice == 3:
            # Handle balance check option.
            print(f"Your current balance is: {account.get_balance():.2f} kr")

        elif choice == 4:
            # Handle exit option.
            break

        else:
            # Handle invalid menu choice.
            print("Invalid choice. Please enter a number between 1 and 4.")



if __name__ == "__main__":
    main_menu()