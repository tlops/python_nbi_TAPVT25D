class Hangman:
    def __init__(self, word):
        self.word = word.lower()
        self.guessed = list() # Skapa en tom lista
        self.fails = 0
        self.max_fails = 6

    def get_masked_word(self):
        return "".join(map(lambda letter: letter if letter in self.guessed else "_", self.word))
    
        # join() tar en lista och gör den till en sträng ["p", "_", "_", "_", "_", "_"] -> "p_____"
    def guess(self, letter):
        if letter.lower() in self.word:
            self.guessed.append(letter.lower())
        else:
            self.fails += 1
    
    def is_won(self):
        return all(letter in self.guessed for letter in self.word)
    
    def is_lost(self):
        return self.fails == self.max_fails