#!/usr/bin/python3
def add_function(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be of type int or float.")
        
    total = a + b
    return total
    
#add_function("qw", "ds")
