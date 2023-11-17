from Guess import Guess
from StringDatabase import StringDatabase
import sys

db = StringDatabase()
randomWord = db.generateRandomWord()
g = Guess()
mode = sys.argv[1]
if mode == "play" or mode == "test":
    g.startGame(mode)
else:
    print("Invalid mode. Enter 'play' or 'test'")

