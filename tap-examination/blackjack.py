#!/usr/bin/python3

"""
Blackjack-like dice game: player vs dealer.
Usage:
    python3 blackjack.py
"""

import random
import json
import os
import sys

# adjustable variables
PLAYER_BUST_VALUE = 21 # Om spelaren får över 21 förlorar denna direkt
DEALER_STOP_VALUE = 17 # Dealern slår automatiskt tills den når minst 17 poäng.

class Player:
    #  Base class for the Player and Dealer in the dice game.
    def __init__(self, name="Player"):
        self.name = name
        self.score = 0

    def roll_dice(self):
        # Simulates rolling a 6-sided die. Returns die value
        die_roll = random.randint(1, 6)
        self.score += die_roll
        return die_roll

    def is_bust(self):
        # Checks if the current score exceeds the bust value (21).
        return self.score > PLAYER_BUST_VALUE

    def reset(self):
        # Resets the player's score for a new round.
        self.score = 0


class Dealer(Player):
    # Represents the Dealer, inheriting from Player
    # Dealer automatically hits until reaching at least 17.
    def __init__(self):
        super().__init__("Dealer")

    def roll_untill_stand(self):
        # Dealer's specific rule: Must keep rolling until score is 17 or more
        # should_roll
        return self.score < DEALER_STOP_VALUE

    
class GameLogic:
    # Manages the overall game flow, players, and winner determination.
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        #self.score_manager = HighScoreManager()

    def _display_current_status(self, current_roll):
        # Displays the result of the last roll and the player's total score.
        print(f"You played {current_roll}. Your total point is now: {self.player.score}")

    """
    def _get_player_choice(self):
        # Prompts the player for input ROLL or STAND ('r' or 's') 
        while True:
            # Ask user to roll or stand
            choice = input("Do you want to (r)oll or (s)tand? ").strip().lower()
    """
    def players_turn(self):
        # Prompts the player for input ROLL or STAND ('r' or 's')
        # Checks if player won or lost
        while True:
            # Ask user to roll or stand
            choice = input("Do you want to (r)oll or (s)tand? ").strip().lower()

            if choice in ("r", "roll"):
                # if player chooses to roll
                roll = self.player.roll_dice()
                # Display rolled Die
                self._display_current_status(roll)
  
                # Check for bust
                if self.player.is_bust():
                    print(f"BUST! Your point is ({self.player.score}) is over {PLAYER_BUST_VALUE}. You lost this round!")
                    return "bust"

            elif choice in ("s", "stand"):
                # if player chooses to stand
                 print(f"You stand with total Point: {self.player.score}")
                 return "stayed"

            else:
                print("Invalid input. Please enter 'r' to roll or 's' to stand.")

    
    def dealers_turn(self):
        # Handles the dealer's automatic turn, following the rule to hit until >= 17.
        print("\n--- Dealer's Turn ---")
        while self.dealer.roll_untill_stand():
            roll = self.dealer.roll_dice()
            print(f"Dealer rolled {roll} and has total: {self.dealer.score}")

            if self.dealer.is_bust():
                print(f"DEALER BUST! Dealer's total point ({self.dealer.score}) is over {PLAYER_BUST_VALUE}.")
                return "bust"

            else:
                print(f"Dealer stands with total: {self.dealer.score}")
                return "stayed"

    
    def decide_winner(self, player_outcome, dealer_outcome):
        # Compares scores to determine the winner of the round and updates the high score
        winner = None

        # Scenario 1: Player busts (already handled in player_turn)
        if player_outcome == "bust":
            print(f"Dealer Wins (Player had over {PLAYER_BUST_VALUE} point).")
            winner = "Dealer"

        # Scenario 2: Player stayed, Dealer busts
        elif dealer_outcome == "bust":
            print(f"Congratulations! You win (Dealer went over {PLAYER_BUST_VALUE} points).")
            winner = "Player"

        else:
            player_score = self.player.score
            dealer_score = self.dealer.score

            print(f"\nFinal Score — You: {player_score} vs Dealer: {dealer_score}")

            # Check for a tie
            if player_score == dealer_score:
                print("It's a tie! No winner in this round.")
                winner = "Tie"

            # Player is closer to 21
            elif player_score > dealer_score:
                print("You are closer to 21. You win!")
                winner = "Player"

            # Dealer is closer to 21
            else:
                print("Dealer is closer to 21. Dealer wins.")
                winner = "Dealer"
        """
        # Update and display scores if there was a definitive winner
        if winner in ["Player", "Dealer"]:
            self.score_manager.update_score(winner)
        """

    
    def reset_round(self):
        # Resets both player and dealer for a new game.
        self.player.reset()
        self.dealer.reset()

    def start_game(self):
        # Runs the full game loop for one round.
        self.reset_round()
        """
        self.score_manager.display_scores()
        """
        # 1. Player's turn
        player_outcome = self.players_turn()

        # If player busted, the round is over
        if player_outcome == "bust":
            self.decide_winner("bust", "stayed")
            return
        
        # 2. Dealer's turn
        dealer_outcome = self.dealers_turn()

        # 3. Determine winner
        self.decide_winner(player_outcome, dealer_outcome)


# Run the game
if __name__ == "__main__":
    try:
        game = GameLogic()
        #game.play_again_loop()
    except Exception as e:
        print(f"\nInterrupted. Saving highscores and exiting: {e}")
        
        # Ensure scores are saved even on unexpected error before exiting.
        #game.score_manager.save_scores()
        sys.exit(1)


#game1 = GameLogic()   








            


















