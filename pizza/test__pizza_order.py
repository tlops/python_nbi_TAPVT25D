#!/usr/bin/python3

import pytest

from pizza_order import PizzaOrder

def test_new_pizza_has_base_price():
    # Test case to verify that a new pizza without toppings has the base price.
    pizza = PizzaOrder()
    assert pizza.get_total_price() == 80 

# Test the price of pizza with a number of toppings
@pytest.mark.parametrize("toppings, expected_price", [
    # Test case with 0 toppings.
    ([], 80),

    # Test case with 1 topping.
    (["cheese"], 90),

    # Test case with 2 toppings.
    (["cheese", "mushrooms"], 100),

     # Test case with 5 toppings.
     (["cheese", "mushrooms", "olives", "ham", "onion"], 130)

     ])


def test_pizza_with_toppings_price(toppings, expected_price):
    # Tests the price calculation with different numbers of toppings.
    pizza = PizzaOrder()
    for topping in toppings:
        pizza.add_toppings(topping)

    assert pizza.get_total_price() == expected_price


def test_pizza_must_have_a_base():
    # Test case to verify that a ValueError is raised if the order is empty.
    with pytest.raises(ValueError) as excinfo:
        PizzaOrder(has_base=False).get_total_price()
    assert "A pizza must have a base." in str(excinfo.value)

