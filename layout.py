from os import system, name

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def PlayScreen(guessType :Guess, chance: int): #TODO : create some centralized place for such functionality
    
    