#include <iostream>
#include <algorithm>
#include <fstream>


#if defined _WIN32 || _WIN64
#include <windows.h>
#define OS "WIN"
#define h GetStdHandle(STD_OUTPUT_HANDLE)
#else
#define OS "UNIX"
#endif

using namespace std;

const int ANSWER_SIZE = 2314;
const int GUESS_SIZE = 10656;

const int WIN_RED = 4;
const int WIN_GREEN = 2;
const int WIN_YELLOW = 14;
const int WIN_WHITE = 7;

const string UNIX_RED = "\u001B[31m";
const string UNIX_GREEN = "\u001B[32m";
const string UNIX_YELLOW = "\u001B[33m";
const string UNIX_RESET = "\u001B[0m";


void clear();
void play();
void display(string word, int guessInfo[6]);
bool inList(string word, string *list, int n);
bool inWord(char c, string word);

string answers[ANSWER_SIZE];
string guesses[GUESS_SIZE];

int main() {
    clear();
    cout << "Operating system family: " << (OS == "WIN" ? "Windows" : "UNIX Based") << endl;
    ifstream ans("./data/answers.txt");
    ifstream guess("./data/guesses.txt");

    bool game = true;

    for (int i=0; i<ANSWER_SIZE; i++) ans >> answers[i];
    for (int i=0; i<GUESS_SIZE; i++) guess >> guesses[i];

    while (game) {
        int option;
        cout << "1. Play Wordle" << endl;
        cout << "2. Run bot" << endl;
        cout << "--------------------" << endl;
        cin >> option;
        switch (option) {
            case 1:
                play();
                break;
            case 2:
                break;
        }
        clear();
    }

}

void play() {
    int guessCount = 0;
    int madeGuessesInfo[6];
    string madeGuesses[6];
    string answer = answers[(rand() % ANSWER_SIZE)];
    string guess;
    string guessStatus = "Your guess must be a 5 letter word.";
    while (guessCount != 6) {
        clear();
        for (int i=0; i<guessCount; i++) {
            cout << to_string(i) << "." << " ";
            display(madeGuesses[i], madeGuessesInfo);

        }
        cout << "--------------------" << endl;
        cout << "Enter a guess: ";
        cin >> guess;
        if (guess.size() != 5) {
            guessStatus = "Guess must be a 5 letter word"; 
        }
        else if (!inList(guess, guesses, GUESS_SIZE) && !inList(guess, answers, ANSWER_SIZE)) {
            guessStatus = "Guess not in wordlist.";
        }
        else {
            for (int i=0; i < 6; i++) {
                if (guess[i] == answer[i]) madeGuessesInfo[i] = 2;
                else if (inWord(guess[i], answer)) madeGuessesInfo[i] = 1;
                else madeGuessesInfo[i] = 0;
            }
            madeGuesses[guessCount] = guess;
            guessCount++;
        }
        cout << guessStatus << endl;
    }
}

bool inList(string word, string *list, int n) {
    return (find(list, list+n, word) != list+n);
}
bool inWord(char c, string word) {
    return (find(word.begin(), word.end(), c) != word.end());
}
void clear() {
    if (OS == "WIN") {
        system("cls");
    }
    else {
        cout << "\x1B[2J\x1B[H";
    }
}

void display(string word, int guessInfo[6]) {
    for (int i=0; i<6; i++) {
        if (guessInfo[i] == 0) cout << word[i];
        else if (guessInfo[i] == 1) {
            if (OS == "WIN") {
                SetConsoleTextAttribute(h, WIN_YELLOW);
                cout << word[i];
                SetConsoleTextAttribute(h, WIN_WHITE);
            } else cout << (UNIX_YELLOW + word[i] + UNIX_RESET);
        }
        else {
            if (OS == "WIN") {
                SetConsoleTextAttribute(h, WIN_GREEN);
                cout << word[i];
                SetConsoleTextAttribute(h, WIN_WHITE);
            } else cout << (UNIX_RED + word[i] + UNIX_RESET);
        }
        cout << " ";
    }
    cout << endl;
}