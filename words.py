from Guess import Guess
from StringDatabase import StringDatabase
import sys

db = StringDatabase()
randomWord = db.generateRandomWord()
g = Guess()
# reads command line argument for play or test
mode = sys.argv[1]
if mode == "play" or mode == "test":
    g.startGame(mode)
else:
    print("Invalid mode. Enter 'play' or 'test'")

