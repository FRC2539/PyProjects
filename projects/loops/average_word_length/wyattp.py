#Wyatt Petula
import string

def averageWords(inputString):
    letterCount = 0
    wordCount = 0
    punc = string.punctuation
    wordAdded = False
    
    for letters in inputString:
        if (letters not in punc) and (letters != " "):
            letterCount += 1
        if wordAdded == False:
            wordCount += 1
            wordAdded = True
            
    
    if wordCount != 0:
        print(letterCount / wordCount)
    else:
        print(letterCount)
        
def avgWords(inputString):
    words = inputString.replace(".", "").split()
    
    total = 0
    
    for word in words:
        total += len(word)
        
    return total / len(words)

print(avgWords("Hello hi World"))
        
#averageWords("12 Weaver Street. Is AmAzInG!!! Wow....")

#averageWords("jflkdsjlkdfjd;ldkfslkjf.ldkfjslkj.ddjjdjd")
