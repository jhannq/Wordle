# responsible for disk I/O and random selection of the word for a new game
import random

class StringDatabase:
    def readFile(self):
        with open("four_letters.txt", "r") as file:
            words = file.read().split()
        # print(words)
        print("Randomly selected word: " + random.choice(words))

db = StringDatabase()

db.readFile()
