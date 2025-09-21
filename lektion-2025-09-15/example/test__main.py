from main import Hangman

# * När ett nytt spel startar ska ordet maskeras med ____ med lika många _ som bokstäver i ordet
# * Gissar man korrekt bokstav ska bokstaven och position avslöjas
# * Fel bokstav avslöjar inget
# * Gissningar ska vara case insensitiva
# * Varje felgissning ska räknas
# * Gissar man alla bokstäver korrekt så ska man vinna
# * Gissar man fel efter max tillåtna felgissningar så förlorar man

def test_new_game_should_mask_the_word():
    game = Hangman("python")
    game2 = Hangman("hello")
    assert game.get_masked_word() == "______"
    assert game2.get_masked_word() == "_____"

def test_correct_guess_should_reveal_letter():
    game = Hangman("python")
    game.guess("p")
    assert game.get_masked_word() == "p_____"

def test_multiple_guesses_should_reveal_all_letters():
    game = Hangman("banana")
    game.guess("a")
    game.guess("n")
    assert game.get_masked_word() == "_anana"

def test_wrong_guess_should_not_reveal_letter():
    game = Hangman("python")
    game.guess("z")
    assert game.get_masked_word() == "______"

def test_guess_should_be_case_insensitive():
    game = Hangman("Dog")
    game.guess("d")
    assert game.get_masked_word() == "d__"
    game.guess("O")
    assert game.get_masked_word() == "do_"

def test_incorrect_guess_should_increase_fail_count():
    game = Hangman("python")
    game.guess("z")
    assert game.fails == 1

def test_should_win_if_correct_guesses():
    game = Hangman("hi")
    game.guess("h")
    game.guess("i")
    assert game.is_won() == True

def test_should_lose_if_max_number_of_guesses_is_reached():
    game = Hangman("python")
    guesses = ["a", "b", "c", "d", "e", "f"]
    for letter in guesses:
        game.guess(letter)
    assert game.is_lost() == True