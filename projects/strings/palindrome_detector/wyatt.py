#Wyatt Petula

def pFinder():
    print("Enter a string below")
    inputString = str(input())
        
    for index in range(0, len(inputString)):
        if not (inputString[index] == inputString[len(inputString) - 1 - index]):
            print("This is not a palindrome")
            return
        
    print("This is a palindrome")
        
pFinder()
