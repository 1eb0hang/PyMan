from enum import Enum

word = "hippopotamus"
attempts = 7
attemptNo = 1
correct = False #check if guess is correct
valid = False #check if input is valid; will be reset when nessesary
end = False  #check if attempts have been used up

class Guess(Enum):
    LETTER = 1
    WORD = 2


def strlen(strWord: str) -> int:
    result = 0
    for i in strWord:
        result +=1
    
    return result

count = strlen(word)
print("\nThe word has " + str(count) +" letters\n")

valid = False
while(valid == False):

    guessType = input("Would you like to guess a letter or a word:\n[1] Letter\n[2] Word\n>> ")
    
    if(guessType == "1" or guessType == "2"):
        gType = Guess(int(guessType))
        print(type(type))
        valid = True
    else:
        print("You have entered an invalid input\n")

print(gType)

#while(end == False and correct == False):
#    guess = input("Please guess the word:\n>> ")
#    
#    if(guess == word):
#        print("Correct!\n")
#        correct = True
#        end = True
#       
#    else:
#        print("Unfortunatly that is incorrect :(\n")
#    
#    attemptNo += 1
#    
#    if(attemptNo>attempts):
#        end = True
        
    
print("End of program!\n")