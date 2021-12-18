#Thomas Zimmerman
def SentenceChecker():
    print('Enter a string for evalutation')
    inputVal = str(input())
    inputVal.lower()
    reversedVal = inputVal[::-1]
    print(str(reversedVal))
    if inputVal == reversedVal:
        print('This input is a palindrome.')
        
    else:
            print("This input is not a palindrome.")
            
            
SentenceChecker()
