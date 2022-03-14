import os
import random
import colorama
from collections import defaultdict


guesses = open("valid_guesses.csv", "r").read().split("\n")
solutions = open("valid_solutions.csv", "r").read().split("\n")


def printc(colorCode="", text="", endline="\n"):
    print(colorCode + text + "\u001b[0m", end=endline)

def clear():
    if os.name == "nt": os.system('cls')
    else: os.system('clear')

def bestGuess(answer, guess, infoDist):
    pass
def play():
    def getInfoDistribution(answer, guess):
        dist = [0] * len(answer)
        answerFreq = defaultdict(lambda: 0, { i : answer.count(i) for i in answer })
        guessFreq = defaultdict(lambda: 0, { i : guess.count(i) for i in guess })
        for i in range(0, len(answer)):
            if guess[i] == answer[i]:
                answerFreq[guess[i]] -= 1
                guessFreq[guess[i]] -= 1
                dist[i] = 2
        for i in range(0, len(answer)):
            if answerFreq[guess[i]] != 0 and guessFreq[guess[i]] != 0:
                dist[i] = 1
                answerFreq[guess[i]] -= 1
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

    
    answer = "slush"#solutions[random.randrange(len(solutions))]
    guessCount = 0
    madeGuesses = []

    guess = ""

    while (True):
        clear()
        printc("\u001b[31m", answer)
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
            guess = input("Enter a guess, enter in 'bot' to find the next best word, or enter 'q' to quit: ").lower()
            if guess == "bot":
                guessCount += 1
                madeGuesses.append(bestGuess(answer, guess, getInfoDistribution(answer, guess)))
            elif guess == "q":
                return
            elif len(guess) != 5: 
                input("Guess must be a 5 letter word, press Enter to continue...")
            elif guess not in guesses and guess not in solutions:
                input("Guess is not a valid word, press Enter to continue...")
            else:
                guessCount += 1
                madeGuesses.append(guess)
            


clear()
colorama.init()

run = True

while (run):
    option = ""
    clear()
    printc("\u001b[33m", "Wordle Sight")
    print("1. Play Wordle!")
    print("2. Run Bot")
    option = input("Choose an option: ")
    if (option == "1"):
        play()
    elif (option == "2"):
        pass
    else:
        input("That is not a valid option, press Enter to continue...")
