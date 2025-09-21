#!/usr/bin/python3

# We will use pytest to run these tests.
import pytest

def test_add_positive_number():
    # Test case to verify that the add function correctly sums two positive numbers.
    from add_function import add_function
    assert add_function(2, 3) == 5
   
def test_add_negative_and_positive_numbers():
    # Test case to verify that the add function correctly sums two positive numbers.
    from add_function import add_function
    assert add_function(-1, 1) == 0
   
def test_add_zero_and_positive_number():
    # Test case to verify that the add function correctly sums two positive numbers.
    from add_function import add_function
    assert add_function(0, 8) == 8
   
def test_add_floating_point_numbers():
    # Test case to verify that the add function correctly sums two positive numbers.
    from add_function import add_function
    assert add_function(2.6, 3.4) == 6
  
  
def test_graceful_response_to_invalid_types_numbers():
    # Test case to verify that the add function correctly sums two positive numbers.
    from add_function import add_function
    with pytest.raises(TypeError) as excinfo:
        add_function("dfd", "dgd")
    
    # Optionally, we can check the error message.
    #assert add_function("dfd", "dgd") == "TypeError: Inputs must be of type int or float."
    #assert "Inputs must be of type int or float." in str(excinfo)



