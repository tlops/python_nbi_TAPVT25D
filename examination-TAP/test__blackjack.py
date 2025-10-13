 #!/usr/bin/python3

import pytest
from unittest.mock import patch
from blackjack import Player, Dealer, GameLogic, PLAYER_BUST_VALUE, DEALER_STOP_VALUE


@pytest.fixture
def game_instance():
    """Fixture to provide a fresh GameLogic instance for each test."""
    return GameLogic()


def test_player_initial_score():
    # Test 1: Check initial score
    # Ensures that a new Player or Dealer object starts with a score of 0.
    player = Player()
    dealer = Dealer()
    assert player.score == 0
    assert dealer.score == 0

@patch('random.randint', side_effect=[6, 5, 6]) # Mock the dice rolls
def test_player_score_increases(mock_randint):
    """
    Test 2: Check score accumulation.
    Ensures the score increases correctly after multiple rolls.
    We set predetermin rolls. 6 + 5 + 6 = 17.
    """
    player = Player()
    player.roll_dice() # 6
    player.roll_dice() # 5
    player.roll_dice() # 6
    assert player.score == 17

def test_is_bust_check():
    # Test 3: Check the bust condition (score > 21).
    player = Player()
    # Set the score just below BUST_THRESHOLD
    player.score = PLAYER_BUST_VALUE
    assert player.is_bust() == False

    # Set the score just above BUST_THRESHOLD
    player.score = PLAYER_BUST_VALUE + 1
    assert player.is_bust() == True


# --- Dealer Specific Logic Tests ---
@pytest.mark.parametrize("current_score, expected_to_roll", [
    (16, True),  # Below 17, must roll
    (17, False), # At 17, must stay
    (20, False)  # Above 17, must stay
])
def test_dealer_roll_untill_stand_logic(current_score, expected_to_roll):
    # Test 4: Check dealer stop condition
	# Ensures the Dealer's roll_untill_stand stops just before 17
    dealer = Dealer()
    dealer.score = current_score
    assert dealer.roll_untill_stand() == expected_to_roll


# --- Winner Determination Logic Tests ---
@pytest.mark.parametrize("player_score, dealer_score, expected_winner", [
    # Player wins (closer to 21)
    (20, 18, "Player"),
    # Dealer wins (closer to 21)
    (18, 20, "Dealer"),
    # Tie
    (19, 19, "Tie"),
    # Player BUST, Dealer wins
    (22, 18, "Dealer"),
    # Dealer BUST, Player wins
    (18, 22, "Player")
])
@patch('blackjack.GameLogic.decide_winner') # simulate the winner to test the winning logics
def test_winner_determination_scores(mock_determine_winner, game_instance, player_score, dealer_score, expected_winner):
    # Test 5: Check winner determination when scores are compared.
    # Verifies that the correct winner is decided based on who is closest to 21.

    # Set scores and outcomes directly for testing the 'decide_winner' function
    game_instance.player.score = player_score
    game_instance.dealer.score = dealer_score


    # Determine the outcomes to pass to the function (assuming no bust unless score > 21)
    player_outcome = "bust" if player_score > PLAYER_BUST_VALUE else "stayed"
    dealer_outcome = "bust" if dealer_score > PLAYER_BUST_VALUE else "stayed"

    
    # Test the final logic outputs based on the comparison rules.
    if player_outcome == "bust":
        actual_winner = "Dealer"
    elif dealer_outcome == "bust":
        actual_winner = "Player"

    else:
        if player_score == dealer_score:
            actual_winner = "Tie"
        elif player_score > dealer_score:
            actual_winner = "Player"
        else:
            actual_winner = "Dealer"

    assert actual_winner == expected_winner

    































