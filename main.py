word = "hippopotamus"
attempts = 7
attemptNo = 1
correct = False
end = False

while(end == False and correct == False):
    guess = input("Please guess the word:\n -> ")
    
    if(guess == word):
        print("Correct!\n")
        correct = True
        end = True
    elif(guess == "\n"):
        print("Unfortunatly that is incorrect :(\n")
       
    else:
        print("Unfortunatly that is incorrect :(\n")
    
    attemptNo += 1
    
    if(attemptNo>attempts):
        end = True
        
    
print("End of program!\n")