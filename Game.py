class Game:

    def displayGameReport(self, listOfWords, listOfStatus, listOfIncorrectGuesses, listOfIncorrectLetters, listOfScores):
        print("\n++")
        print("++ Game Report")
        print("++\n")
        print("Game    Word    Status     Bad Guesses    Missed Letters    Score")
        print("----    ----    -------    -----------    --------------    ------")
        for i in range(len(listOfWords) - 1):
              print(str(i+1) + "       " +  str(listOfWords[i]) + "    " + str(listOfStatus[i]) + "    " +str(listOfIncorrectGuesses[i]) +"              " + str(listOfIncorrectLetters[i]) +"                 " + str(listOfScores[i]))
        finalScore = round(sum(listOfScores),2)
        print("\nFinal Score: " + str(finalScore))
