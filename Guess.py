# menu display, user input, scoring logic
class Guess: 
    def displayMenu(self):
        print("++")
        print("++ The Great Guessing Game")
        print("++")
        print("\n")
        print("Current Guess: " + "----")
        print("Letters Guessed: ")
        
    def readInput(self):
        print("g = guess, t = tell me, l for letter, and q to quit")
        userInput = input("Enter Option:")
        while userInput not in ("g", "t", "l", "q"):
            print("Invalid option. Please re-enter:")
            userInput = input("Enter Option:")
        if userInput == "g":
            print("Guess: attempt to guess the word")
        elif userInput == "t":
            print("Tell	me:	you	give up and	ask	the	game to	simply show you	the	correct	word")
        elif userInput == "l":
            print("Letter: select an individual	letter that	might be in	the	word")
        elif userInput == "q":
            print("Quit: end the game session and display a final report (more on this below)")


g = Guess()
g.displayMenu()
g.readInput()

