#!/usr/bin/python3
from random import randint

number_to_guess = randint(1, 100)
number_of_guess = 1
#print(f"Number To guess = {number_to_guess}")

while number_of_guess <= 7:
    try:
        guessed_number = int(input("Guess a number between 1 and 100: "))
        if guessed_number < number_to_guess:
            print("Go higher!")
            number_of_guess += 1
        
        elif guessed_number > number_to_guess:
            print("Go lower!")
            number_of_guess += 1

        else:
            print(f"Congratulations, you won after {number_of_guess} guesses!")
            break

    except ValueError:
        print("Invalid guess!")

else:
    print(f"You lost, the number is {number_to_guess}! ")