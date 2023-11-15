# parses command line and starts the guessing game
from Guess import Guess
# import game import Game
from StringDatabase import StringDatabase
import sys

db = StringDatabase()
randomWord = db.generateRandomWord()
g = Guess()
g.startGame(sys.argv[1])
