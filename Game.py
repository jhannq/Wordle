# information about specific game

# The letters that are still blank at the time of a correct guess will be summed together to give a total. 
# Of course, the number of letters that you request also affects your score.  So you 
# should divide the sum of the frequencies by the number of times you requested a letter.
# Finally, an incorrect guess costs you 10% of your final score for the current word (2 incorrect guess are 20% 
# of the total and so on).
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
# What happens if you give up? Then you should lose points. Here, the total points lost should simply 
# be the sum the letters that have not yet been guessed/uncovered. 