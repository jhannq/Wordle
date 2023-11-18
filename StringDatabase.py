import random

class StringDatabase:

    # get all the words in the file and put them in a list
    def generateRandomWord(self):
        with open("four_letters.txt", "r") as file:
            word = file.read().split()
        #randomly pick a word from the list
        return random.choice(word)

