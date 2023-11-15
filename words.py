# parses command line and starts the guessing game
from Guess import Guess
# import game import Game
from StringDatabase import StringDatabase
import sys

db = StringDatabase()
randomWord = db.generateRandomWord()
g = Guess()
mode = sys.argv[1]
g.startGame(mode)
