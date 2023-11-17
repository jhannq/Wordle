import random

class StringDatabase:
    def generateRandomWord(self):
        with open("four_letters.txt", "r") as file:
            words = file.read().split()
        return random.choice(words)

