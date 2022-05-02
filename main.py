import os
import random
import colorama # https://pypi.org/project/colorama/
from collections import defaultdict

# https://www.kaggle.com/datasets/bcruise/wordle-valid-words?resource=download
guesses = open("valid_guesses.csv", "r").read().split("\n")

# https://www.kaggle.com/datasets/bcruise/wordle-valid-words?resource=download
solutions = open("valid_solutions.csv", "r").read().split("\n")

def printc(colorCode="", text="", endline="\n"): # For colored output
    print(colorCode + text + "\u001b[0m", end=endline)


def clear(): # Clear depending on OS (UNIX Based/Windows)
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def getInfoDistribution(answer, guess):
    answerFreq = defaultdict(lambda: 0, {i: answer.count(i) for i in answer})
    guessFreq = defaultdict(lambda: 0, {i: guess.count(i) for i in guess})

    if (answer == guess):
        return [2] * 5 
    else:
        dist = [0] * len(answer)
        for i in range(0, len(answer)):
            if guess[i] == answer[i]:
                guessFreq[guess[i]] -= 1
                answerFreq[guess[i]] -= 1
                dist[i] = 2
        for i in range(0, len(answer)):
            if dist[i] != 2 and answerFreq[guess[i]] != 0 and guessFreq[guess[i]] != 0:
                guessFreq[guess[i]] -= 1
                answerFreq[guess[i]] -= 1
                dist[i] = 1
        return dist


def displayGuess(answer, guess):
    infoDist = getInfoDistribution(answer, guess)
    for i in range(0, len(answer)):
        if infoDist[i] == 2:
            printc("\u001b[32m", guess[i], endline=" ")
        elif infoDist[i] == 1:
            printc("\u001b[33m", guess[i], endline=" ")
        else:
            printc("", guess[i], endline=" ")
    print("\n")


def play():
    answer = solutions[random.randrange(len(solutions))]
    guessCount = 0
    madeGuesses = []

    guess = ""

    while (True):
        clear()
        for i in range(0, guessCount):
            print(f"{i+1}. ", end="")
            displayGuess(answer, madeGuesses[i])
        printc("\u001b[37m", "-------------------------------")
        if guess == answer:
            printc("\u001b[32m", "Amazing, ", endline="")
            input("you got the right answer! Press Enter to continue...")
            return
        elif guessCount == 6:
            printc("\u001b[31m", "Out of guesses, ", endline="")
            input(f"the correct answer was: '{answer}', press Enter to continue...")
            return
        else:
            guess = input("Enter a guess, or enter 'q' to quit: ").lower()
            if guess == "q":
                return
            elif len(guess) != 5:
                input("Guess must be a 5 letter word, press Enter to continue...")
            elif guess not in guesses and guess not in solutions:
                input("Guess is not a valid word, press Enter to continue...")
            else:
                guessCount += 1
                madeGuesses.append(guess)


clear()
colorama.init() # Colors!

run = True

while (run):
    option = ""
    clear()
    printc("\u001b[33m", "Guess the Word!")
    option = input("Press 'Enter' to play Guess the Word or enter 'q' to quit! ")
    if (option.lower() == "q") :
        run = False
    else:
        play()
