class Game:
    def __init__(self, word, status, badGuesses, missedLetters, score):
        self.word = word
        self.status = status
        self.badGuesses = badGuesses
        self.missedLetters = missedLetters
        self.score = score