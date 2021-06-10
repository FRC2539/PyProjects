#Wyatt Petula
import random

def rPSGame(playerInput):
    botInput = int(random.random() * 3 + 1)
    if botInput == 1 && playerInput == "Scissors":
        return [botInput, "Bot"]
    if botInput == 2 && playerInput == "Scissors":
        return [botInput, "Player"]
    if botInput == 3 && playerInput == "Scissors";
    
    
rPSGame(6)
