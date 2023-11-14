import os
from StringDatabase import StringDatabase
# menu display, user input, scoring logic
        
class Guess: 
    def __init__(self):
        self.db = StringDatabase()
        self.currentWord = self.db.generateRandomWord()
        self.currentGuess = ["-", "-", "-", "-"]
        self.lettersGuessed = []
        
    def setCurrentWord(self, newCurrentWord):
        self.currentWord = newCurrentWord

    def displayGameTitle(self):
        print("++")
        print("++ The Great Guessing Game")
        print("++")
        
    def readInput(self):
        userInput = ""
        while userInput != "q":
            self.displayGameTitle()

            print("\nCurrent Word: " + self.currentWord)
            print("Current Guess: " + ''.join(map(str, self.currentGuess)))
            print("Letters Guessed: " + ' '.join(map(str, self.lettersGuessed)) + "\n")

            print("g = guess, t = tell me, l for letter, and q to quit\n")
            userInput = input("Enter Option: ")
            
            while userInput not in ("g", "t", "l", "q"):
                userInput = input("\nInvalid option. Please re-enter: ")
            
            if userInput == "g":
                guess = input("\nMake you guess: ").lower()
                if guess == self.currentWord:
                    self.displayGuessMessage(True)
                    self.restart()
                else:
                    self.displayGuessMessage(False)

            elif userInput == "t":
                self.displayTellMessage(self.currentWord)
                self.restart()

            elif userInput == "l":
                letter = input("\nEnter a letter: ").lower()
                if letter in self.currentWord:
                    index = self.currentWord.index(letter)
                    self.currentGuess[index] = letter
                    self.displayLetterMessage(True)
                else:
                    self.lettersGuessed.append(letter)
                    self.displayLetterMessage(False)
                    
    def displayLetterMessage(self, check):
        print("\n@@")
        if check == True:
            print("@@ FEEDBACK: Woo hoo, you found 1 letter")
        else:
            print("@@ FEEDBACK: Not a single match, genius")
        print("@@\n")
        input("Press any key to continue...")
        os.system('clear')
    
    def displayGuessMessage(self, check):
        print("\n@@")
        if check == True:
            print("@@ FEEDBACK: You're right, Einstein!")
        else:
            print("@@ FEEDBACK: Try again, Loser!")
        print("@@\n")
        input("Press any key to continue...")
        os.system('clear')

    def displayTellMessage(self, currentWord):
        print("\n@@")
        print("@@ FEEDBACK: You really should have guessed this... '" + currentWord + "'")
        print("@@\n")
        input("Press any key to continue...")
        os.system('clear')
    
    def restart(self):
        self.currentGuess = ["-", "-", "-", "-"]
        self.lettersGuessed = []
        randomWord = self.db.generateRandomWord()
        self.setCurrentWord(randomWord)
    


