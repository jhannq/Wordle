# parses command line and starts the guessing game

from guess import Guess
# import game import Game
from stringdatabase import StringDatabase

db = StringDatabase()
randomWord = db.generateRandomWord()
g = Guess(word=randomWord)
g.readInput()