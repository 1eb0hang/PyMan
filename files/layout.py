from enum import Enum
from os import system, name

class Guess(Enum):
    LETTER = 1
    WORD = 2

class ScreenType(Enum):
    LETTER_GUESS = 1
    WORD_GUESS = 2
    WIN_SCREEN = 3
    LOSE_SCREEN = 4

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
        
def LetterGuess() -> bool:
    

def WordGuess() -> bool:


#def ScreenSelcetion() -> ScreenType:

def Screen(guessType :Guess, chance: int): #TODO : create some centralized place for such functionality
    #end = False
    print("You have "+str(chance)+" chances left")
    
    if (guessType == Guess.LETTER):
        LetterGuess()
    else:
        WordGuess()
    
    