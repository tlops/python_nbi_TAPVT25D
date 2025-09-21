#!/usr/bin/python3

class PizzaOrder():
    

    def __init__(self, has_base=True):
         # set base price of pizza
        self.price = 80

        # creates an empty list to store number of toppings
        self.toppings = []

        # Set parameter to test for base
        self.has_base = has_base

    
    def add_toppings(self, topping):
        # Adds a topping to the pizza.
        self.toppings.append(topping)

    def get_total_price(self):
        if not self.has_base:
            raise ValueError("A pizza must have a base.") 

        self.price = self.price + (len(self.toppings) * 10)
        return self.price

