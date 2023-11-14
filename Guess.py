import os
# menu display, user input, scoring logic
        
class Guess: 
    def __init__(self, word):
        self.word = word

    def displayStart(self):
        print("++")
        print("++ The Great Guessing Game")
        print("++")
        
    def readInput(self):
        userInput = ""
        while userInput != "q":
            self.displayStart()

            print("\nCurrent Word: " + self.word)
            print("Current Guess: " + "----")
            print("Letters Guessed: \n")

            print("g = guess, t = tell me, l for letter, and q to quit\n")
            userInput = input("Enter Option: ")
            
            while userInput not in ("g", "t", "l", "q"):
                userInput = input("\nInvalid option. Please re-enter: ")
            
            if userInput == "g":
                guess = input("\nGuess: ")
            
            elif userInput == "t":
                print("\nTell	me:	")

            elif userInput == "l":
                letter = input("\nLetter: ").lower()
                if letter in self.word:
                    self.displayLetter(True)
                else:
                    self.displayLetter(False)

    def displayLetter(self, check):
        print("@@")
        if check == True:
            print("@@ FEEDBACK: Woo hoo, you found 1 letter")
        else:
            print("@@ FEEDBACK: Not a single match, genius")
        print("@@\n")
        input("Press any key to continue...")
        os.system('clear')
    
    


