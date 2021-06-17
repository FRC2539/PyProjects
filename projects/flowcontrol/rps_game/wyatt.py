#Wyatt Petula--Test Ready
import random 

def rpsGame():
    print("Enter lowercase move below")
    
    try:
        playerInput = input()
        botInput = random.randint(1, 4)
        
        if (botInput == 1 and playerInput == "rock") or (botInput == 2 and playerInput == "paper") or (botInput == 3 and playerInput == "scissors"):
            print("TIE WITH " + playerInput)
        
        if (botInput == 1 and playerInput == "paper") or (botInput == 2 and playerInput == "scissors") or (botInput == 3 and playerInput == "rock"):
            print("BOT LOSES AGAINST " + playerInput)
        
        if (botInput == 1 and playerInput == "scissors") or (botInput == 2 and playerInput == "rock") or (botInput == 3 and playerInput == "paper"):
            print("BOT WINS AGAINST " + playerInput)
        
        if playerInput == "machine gun":
            print("TOTAL DOMINATION!")

    except(ValueError):
        print("Do you even rock paper scissors?")

rpsGame()
