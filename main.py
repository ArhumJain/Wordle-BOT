import os
import random
import colorama


def printc(colorCode="", text="", endline="\n"):
    print(colorCode + text + "\u001b[0m", end=endline)

def clear():
    if os.name == "nt": os.system('cls')
    else: os.system('clear')

def play():
    def displayGuess(answer, guess):
        for i in range(0, len(answer)):
            if answer[i] == guess[i]: 
                printc("\u001b[32m", guess[i], endline=" ")
            elif guess[i] in answer[i]:
                printc("\u001b[33m", guess[i], endline=" ")
            else:
                printc("", guess[i], endline="")
        print("\n")

    guesses = open("valid_guesses.csv", "r").read().split("\n")
    solutions = open("valid_solutions.csv", "r").read().split("\n")
    
    answer = solutions[random.randrange(len(solutions))]
    guessCount = 0
    madeGuesses = []

    for i in range(0, guessCount):


clear()
colorama.init()

run = True



while (run):
    option = ""
    while (option != "1" or option != "2"): 
        clear()
        printc("\u001b[33m", "Wordle Sight")
        print("1. Play Wordle!")
        print("2. Run Bot")
        option = input("Choose an option: ")
    if (option == "1"):
