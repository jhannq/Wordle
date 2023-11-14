# responsible for disk I/O and random selection of the word for a new game
import random

class StringDatabase:
    def generateRandomWord(self):
        with open("four_letters.txt", "r") as file:
            words = file.read().split()
        return random.choice(words)

