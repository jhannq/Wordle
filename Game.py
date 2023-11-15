# information about specific game
blank = ["-", "-", "-", "-"]
word = "pppp"
indexes = []
userInput = "p"

for index, letter in enumerate(word):
    if letter == userInput:
        indexes.append(index)

for index in indexes:
    blank[index] = userInput

print(blank)