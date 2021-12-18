import random

print("GOD COMPELES YOU TO CHOOSE AN OPTION. r, p, or s?")

playerInput = input()

randomChoiceArray = ["r", "p", "s"]

if playerInput not in randomChoiceArray:
    print("pick an actual option")
    
randomChoice = random.choice(randomChoiceArray)

print(randomChoice)

def decideWinner(playerInput, randomChoice):
    if playerInput == "r" and randomChoice == "p":
        return False
    elif playerInput == "r" and randomChoice == "s":
        return True
    elif playerInput == "p" and randomChoice == "r":
        return True
    elif playerInput == "p" and randomChoice == "s":
        return False
    elif playerInput == "s" and randomChoice == "r":
        return False
    elif playerInput == "s" and randomChoice == "p":
        return True
    
    return -1
    
winner = decideWinner(playerInput, randomChoice)

if not winner:
    print("you lost to a bot bro.")
elif winner == True:
    print("you beat random things, CONGRATS.")
else:
    print("BRUUUUUUUUUUUUUUUUU")





        
        
