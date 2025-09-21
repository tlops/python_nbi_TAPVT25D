#!/usr/bin/python3

import pytest

# import Counter from counter class
from counter import Counter


def test_counter_starts_at_zero():
    # Test case to verify that a new Counter instance starts with a value of 0.
    my_counter = Counter()
    # The initial value should be zero
    assert my_counter.value == 0

# define series of tests using pytest parameterize module 
@pytest.mark.parametrize("initial_value, increments, expected_value", [
    (0, 1, 1),
    (5, 3, 8),
    (0, 10, 10)
    ])

def test_increment(initial_value, increments, expected_value):
    # Test case to verify that the increment method correctly increases the value.
    my_counter = Counter()
    my_counter.value = initial_value
    for i in range(increments):
        my_counter.increment()
    assert my_counter.value == expected_value 

# define series of tests using pytest parameterize module 
@pytest.mark.parametrize("initial_value, decrements, expected_value", [
    (1, 1, 0),
    (5, 2, 3),
    (10, 5, 5)
    ])

def test_decrement(initial_value, decrements, expected_value):
    # Test case to verify that the decrement method correctly decreases the value.
    my_counter = Counter()
    my_counter.value = initial_value
    for i in range(decrements):
        my_counter.decrement()
    assert my_counter.value == expected_value 

def test_decrement_raises_error_when_below_zero():
    # Test case to ensure a ValueError is raised when decrementing below 0.
    my_counter = Counter()
    # The counter's initial value is 0.
    # We use pytest.raises to check if the correct exception is thrown.
    with pytest.raises(ValueError) as excinfo:
        my_counter.decrement()

    # Optionally, we can check the error message.
    assert "Cannot decrement below 0." in str(excinfo.value)



