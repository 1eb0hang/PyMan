word = "hippopotamus"
attempts = 7
attemptNo = 1
correct = False
end = False

def LetterCount(strWord: str) -> int:
    result = 0
    for i in strWord:
        result +=1
    
    return result

count = LetterCount(word)
print("\nThe word has " + str(count) +" letters\n")

while(end == False and correct == False):
    guess = input("Please guess the word:\n -> ")
    
    if(guess == word):
        print("Correct!\n")
        correct = True
        end = True
       
    else:
        print("Unfortunatly that is incorrect :(\n")
    
    attemptNo += 1
    
    if(attemptNo>attempts):
        end = True
        
    
print("End of program!\n")