#displays text as "crossed out"
def strike(text): 
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

#displays number of characters in a string
def strlen(strWord: str) -> int:
    result = 0
    for i in strWord:
        result +=1
    
    return result