#!/usr/bin/python3

class Counter:
    # A simple class to manage an integer value that can be incremented or decremented.

    def __init__(self):
        # Initializes the Counter with a value of 0.
        self.value = 0

    def increment(self):
        # Increment the Counter with a value of 1.
        self.value += 1


    def decrement(self):
        # decrement the Counter with a value of 1.
        if self.value <= 0:
            raise ValueError("Cannot decrement below 0.")
        self.value -= 1


