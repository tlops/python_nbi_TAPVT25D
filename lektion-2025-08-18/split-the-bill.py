#!/usr/bin/python3

import sys

def main():
    """
    A program that calculate how much each person should pay with Tips.
    """
    print("Welcome to Split the Bill!")
    print("End by typing: end")
    
    # Create a list to add the amount.
    amounts = []
    
    # Main loop to calculate payment from user.
    while True:
        amount_input = input("Type in an amount: ")
        
        # Check if a user wants to terminate the program.
        if amount_input.lower() == "end":
            break
        
        # Convert the entered value to float.
        try:
            amount = float(amount_input)
            amounts.append(amount)
        except ValueError:
            #  Handle error if a user enters non numeric entry.
            print("Invalid Entry. Kindly enter a number or type 'end'.")

    # If no amount is entered, exit the program.
    if not amounts:
        print("No Amount is entered. Welcome to try again!")
        sys.exit(0)
    
    # Version 1: Beräkna den totala summan.
    total_sum = sum(amounts)

    # Version 3: Fråga om dricks.
    tip_input = input("What percentage of Total do you want to give as Tips? (Press Enter for 10%): ")
    
    # Set tips tol 10% as standard if nothing is entered.
    if not tip_input:
        tip_percentage = 10
        print("Using 10% as standard for tips.")
    else:
        # calculate entered percentage of tips.
        try:
            tip_percentage = float(tip_input)
        except ValueError:
            print("Invalid entry for tips. Using 10% as standard.")
            tip_percentage = 10
            
    # Calculate total sum incluve tips.
    final_total = total_sum * (1 + tip_percentage / 100)

    # Version 2: Ask how many people to share the bill.
    while True:
        try:
            num_people_input = input("How many people are in this group? ")
            num_people = int(num_people_input)
            if num_people <= 0:
                print("Number of persons must be whole number.")
                continue
            break
        except ValueError:
            print("Invalid entry. Kindly type in a whole number no dots.")

    # Calculate amoun to be paid per person.
    amount_per_person = final_total / num_people

    # Print out the result.
    print(f"The total to pay inclusive tips is {final_total:.2f} kr. That will be {amount_per_person:.2f} kr per person.")
    print("Thanks for using split the bill!")

if __name__ == "__main__":
    main()
234
232
3434