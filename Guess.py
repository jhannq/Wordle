import os
from StringDatabase import StringDatabase
# menu display, user input, scoring logic
        
class Guess: 
    # initialize class with a word, empty current guess and letters guessed
    def __init__(self):
        self.db = StringDatabase()
        self.currentWord = self.db.generateRandomWord()
        self.currentGuess = ["-", "-", "-", "-"]
        self.lettersGuessed = []

    # start the game loop
    def startGame(self, mode):
        userInput = ""
        # end game when user inputs "q"
        while userInput != "q":
            self.displayGameInformation(mode)

            # ask for options, keep asking until input is valid
            print("g = guess, t = tell me, l for letter, and q to quit\n")
            userInput = input("Enter Option: ")
            while userInput not in ("g", "t", "l", "q"):
                userInput = input("\nInvalid option. Please re-enter: ")
            
            # player wants to guess
            if userInput == "g":
                guess = input("\nMake you guess: ").lower()
                # display a message, give a new word if the guess is correct
                if guess == self.currentWord:
                    self.displayGuessMessage(True)
                    self.restart()
                else:
                    self.displayGuessMessage(False)

            # tells player the word and gives a new word
            elif userInput == "t":
                self.displayTellMessage()
                self.restart()

            # ask player for letter
            elif userInput == "l":
                # keep asking the player for valid input, if the input is not a single letter
                letter = input("\nEnter a letter: ").lower()
                while True:
                    if len(letter) != 1 or not letter.isalpha():
                        letter = input("\nInvalid letter. Please re-enter: ").lower()
                    else:
                        break
                # if the letter is in the word, display it on the current guess
                if letter in self.currentWord:
                    index = self.currentWord.index(letter)
                    self.currentGuess[index] = letter
                    # if the player has guessed all the letters, display message and give a new word
                    if ''.join(map(str, self.currentGuess)) == self.currentWord:
                        self.displayGuessMessage(True)
                        self.restart()
                    else:
                        self.displayLetterMessage(True)
                    
                # if the letter is not in the word, display it in the guessed letters
                else:
                    self.lettersGuessed.append(letter)
                    self.displayLetterMessage(False)
    
    # display game information such as current word, current guess and letters guessed
    def displayGameInformation(self, mode):
        print("++")
        print("++ The Great Guessing Game")
        print("++\n")
        if mode == "play":
            print("Current Guess: " + ''.join(map(str, self.currentGuess)))
            print("Letters Guessed: " + ' '.join(map(str, self.lettersGuessed)) + "\n")
        else:
            print("\nCurrent Word: " + self.currentWord)
            print("Current Guess: " + ''.join(map(str, self.currentGuess)))
            print("Letters Guessed: " + ' '.join(map(str, self.lettersGuessed)) + "\n")
    
    
    # restart the game by giving a new random word, empties current guess and letters guessed
    def restart(self):
        self.currentGuess = ["-", "-", "-", "-"]
        self.lettersGuessed = []
        randomWord = self.db.generateRandomWord()
        self.setCurrentWord(randomWord)
    
    # set a new current word
    def setCurrentWord(self, newCurrentWord):
        self.currentWord = newCurrentWord

    # display a message based on letter input and clear terminal
    def displayLetterMessage(self, check):
        print("\n@@")
        # if they guessed right
        if check == True:
            print("@@ FEEDBACK: Woo hoo, you found 1 letter")
        # if they guessed wrong
        else:
            print("@@ FEEDBACK: Not a single match, genius")
        print("@@\n")
        input("Press any key to continue... ")
        os.system('clear')
    
    # display a message based on guess input and clear terminal
    def displayGuessMessage(self, check):
        print("\n@@")
        # if they guessed right
        if check == True:
            print("@@ FEEDBACK: You're right, Einstein!")
        # if they guessed wrong
        else:
            print("@@ FEEDBACK: Try again, Loser!")
        print("@@\n")
        input("Press any key to continue... ")
        os.system('clear')

    # display word and clear terminal
    def displayTellMessage(self):
        print("\n@@")
        print("@@ FEEDBACK: You really should have guessed this... '" + self.currentWord + "'")
        print("@@\n")
        input("Press any key to continue... ")
        os.system('clear')
    
    def displayCurrentWord(self):
        print("\n@@")
        print("@@ FEEDBACK: You're right, Einstein! The word was '" + self.currentWord + "'")
        print("@@\n")
        input("Press any key to continue... ")
        os.system('clear')


