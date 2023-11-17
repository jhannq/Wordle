# parses command line and starts the guessing game
from Guess import Guess
# import game import Game
from StringDatabase import StringDatabase
import sys

# add error checking
db = StringDatabase()
randomWord = db.generateRandomWord()
g = Guess()
mode = sys.argv[1]
if mode == "play" or mode == "test":
    g.startGame(mode)
else:
    print("Invalid mode. Enter 'play' or 'test'")

