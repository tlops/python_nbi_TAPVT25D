## Blackjack Dice Game (21 with Dice)

## Project Overview
This is a console-based, simplified version of the card game Blackjack (21), played using a 6-sided die instead of cards. The project is designed using Object-Oriented Programming (OOP) principles and implements Test-Driven Development (TDD) practices with pytest for robust code verification.


## Game Rules
The goal is to score as close to 21 as possible without exceeding it.

 1. Gameplay: The player is prompted to either Roll the die (adds 1-6 points) or Stay.

 2. Player Bust: If the player's total score exceeds 21, the player immediately loses the round.

 3. Dealer's Turn: If the player stays, the Dealer takes their turn. The Dealer automatically rolls the die until their score reaches 17 or more.

 4. Dealer Bust: If the Dealer's total score exceeds 21, the player wins.

 5. Winner Determination: If neither player busts, the player closest to 21 wins. A tie results in a draw.

## Features
This project is submitted as part of python programming course Test Automation with Python and meets the requirements for advanced grading criteria by including:

Object-Oriented Design: The game logic is modeled using dedicated classes: Player, Dealer and GameLogic

Robust Input Handling: Includes error handling for invalid user input (e.g., if the user types something other than 'r', 'roll' or 's' 'stand' when prompted).

Test Suite: Includes unit tests (test__blackjack.py) written using pytest to ensure core game logic are working correctly.

## Prerequisites
To run and test this application, you need:

Python 3.x

Pytest (Required for running tests)

You can install the necessary dependency (pytest) using pip:

  pip install pytest-cov

## How to Run the Game
Ensure the main game file (blackjack.py) is in your current directory.

Run the game from your console:

  python blackjack.py


## How to Run the Tests
The project includes a comprehensive set of unit tests in test_blackjack.py to verify the game's core functionality, including dice rolling, scoring, and dealer logic.

Ensure both blackjack.py and test_blackjack.py are in the same directory.

Run pytest from your console:
   pytest --cov=blackjack
