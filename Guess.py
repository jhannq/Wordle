import os
from StringDatabase import StringDatabase
from Game import Game
        
class Guess: 
    # initialize class with a word, empty current guess and letters guessed
    def __init__(self):
        self.db = StringDatabase()
        self.currentWord = self.db.generateRandomWord()
        self.currentGuess = ["-", "-", "-", "-"]
        self.lettersGuessed = []
        self.badGuesses = 0
        self.missedLetters = 0
        self.score = 0
        self.listOfGames = []
        self.letterFrequencies = {'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.70, 'f': 2.23, 'g': 2.02, 'h': 6.09,
                     'i': 6.97, 'j': 0.15, 'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75, 'o': 7.51, 'p': 1.93,
                     'q': 0.10, 'r': 5.99, 's': 6.33, 't': 9.06, 'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15,
                     'y': 1.97, 'z': 0.07, '-': 0}

    # start the game loop
    def startGame(self, mode):
        os.system('clear')
        userInput = ""
        # end game when user inputs "q"
        while userInput != "q":
            # display based on test or play mode
            self.displayGameInformation(mode)

            # ask for options, keep asking until input is valid
            print("g = guess, t = tell me, l for letter, and q to quit\n")
            userInput = input("Enter Option: ")
            while userInput not in ("g", "t", "l", "q"):
                userInput = input("\nInvalid option. Please re-enter: ")
            
            # player wants to guess
            if userInput == "g":
                guess = input("\nMake your guess: ").lower()
                # display a message, give a new word if the guess is correct
                if guess == self.currentWord:
                    self.displayGuessMessage(True)
                    self.calculateScoreWin()
                    self.restart()
                else:
                    self.displayGuessMessage(False)
                    self.badGuesses += 1

            # tells player the word and gives a new word
            elif userInput == "t":
                self.displayTellMessage()
                self.calculateScoreLose()
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
                if letter in self.lettersGuessed:
                    self.displayLetterMessageDupe()
                # if the letter is in the word, display it on the current guess
                elif letter in self.currentWord:
                    indexes = []
                    for index, letters in enumerate(self.currentWord):
                        if letters == letter:
                            indexes.append(index)
                    for index in indexes:
                        self.currentGuess[index] = letter
                    # if the player has guessed all the letters, display message and give a new word
                    if ''.join(map(str, self.currentGuess)) == self.currentWord:
                        self.displayGuessMessage(True)
                        self.calculateScoreWin()
                        self.restart()
                    else:
                        self.displayLetterMessage(True)
                # if the letter is not in the word, display it in the guessed letters
                else:
                    self.lettersGuessed.append(letter)
                    self.displayLetterMessage(False)
                    self.missedLetters += 1
        os.system('clear')
        self.displayGameReport()

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
        self.badGuesses = 0
        self.missedLetters = 0
        self.score = 0
    
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

    def displayLetterMessageDupe(self):
        print("\n@@")
        print("@@ FEEDBACK: You already found this letter")
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
    
    # calculate score when player wins
    def calculateScoreWin(self):
        totalFrequencyOfWord = 0
        sumFrequencyOfGuess = 0
        # player wins without using letters
        if ''.join(map(str, self.currentGuess)) == "----"  or ''.join(map(str, self.currentGuess)) == self.currentWord:
            totalFrequencyOfWord = sum(self.letterFrequencies[letter] for letter in self.currentWord)
            self.score = round(totalFrequencyOfWord,2)
        # player wins using letters and guesses
        else:
            totalFrequencyOfWord = sum(self.letterFrequencies[letter] for letter in self.currentWord)
            sumFrequencyOfGuess = sum(self.letterFrequencies[letter] for letter in self.currentGuess)
            # avoid division by 0
            if self.missedLetters == 0:
                self.score = round(((totalFrequencyOfWord - sumFrequencyOfGuess)) - (((totalFrequencyOfWord - sumFrequencyOfGuess)) * (self.badGuesses * 0.1)),2)
            else:
                self.score = round(((totalFrequencyOfWord - sumFrequencyOfGuess) / self.missedLetters) - (((totalFrequencyOfWord - sumFrequencyOfGuess) / self.missedLetters) * (self.badGuesses * 0.1)),2)
        game = Game(self.currentWord, "Success", self.badGuesses, self.missedLetters, self.score)
        self.listOfGames.append(game)
    
    # calculate score when player loses
    def calculateScoreLose(self):
       # player gives up without using letters or guessing 
        if self.currentGuess == ["-", "-", "-", "-"]:
            totalFrequencyOfWord = sum(self.letterFrequencies[letter] for letter in self.currentWord)
            self.score = -1 * round(totalFrequencyOfWord,2)
        # player gives up using letters and guesses
        else: 
            totalFrequencyOfWord = sum(self.letterFrequencies[letter] for letter in self.currentWord)
            sumFrequencyOfGuess = sum(self.letterFrequencies[letter] for letter in self.currentGuess)
            self.score = -1 * round(totalFrequencyOfWord - sumFrequencyOfGuess,2)
        game = Game(self.currentWord, "Gave Up", self.badGuesses, self.missedLetters, self.score)
        self.listOfGames.append(game)
    
    # display game report
    def displayGameReport(self):
        print("\n++")
        print("++ Game Report")
        print("++\n")
        print("Game    Word    Status     Bad Guesses    Missed Letters    Score")
        print("----    ----    -------    -----------    --------------    ------")
        # loop through the list of games played and display each stat
        for index, game in enumerate(self.listOfGames):
            print(f"{index+1}       {game.word}    {game.status}    {game.badGuesses}              {game.missedLetters}                 {game.score}")
        # sum all the score
        print("\nFinal Score: " + str(sum(game.score for game in self.listOfGames)))