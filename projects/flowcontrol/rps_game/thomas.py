import random

def rockPaperScissors(forcedChoice):
    if not forcedChoice == "":
        chosenHandGesture = forcedChoice
        print('You were compelled by an unknown force to pick', forcedChoice)
    else:
        print('How about a game of rock paper scissors?')
        chosenHandGesture = input()
    
    if chosenHandGesture == "rock" or chosenHandGesture == "paper" or chosenHandGesture == "scissors":
            chosenHandGesture = chosenHandGesture.lower()
            botInput = random.randint(1,3)
            print(botInput)
            if botInput == 1:
                botInput = "rock"
                print('I chose rock!')
            if botInput == 2:
                botInput = "paper"
                print('I chose paper!')
            if botInput == 3:
                botInput = "scissors"
                print('I chose scissors!')
            if botInput == chosenHandGesture:
                print('Tie!')
                rockPaperScissors("")
            else:
                if botInput == "scissors" and chosenHandGesture == "paper":
                    print('Bot Wins!')
                 
                if botInput == "rock" and chosenHandGesture == "scissors":
                   print('Bot wins!')
                 
                if botInput == "paper" and chosenHandGesture == "rock":
                    print('Bot Wins!')
                   
                if chosenHandGesture == "scissors" and botInput == "paper":
                   print('You win!')
                   rockPaperScissors("")
              
                if chosenHandGesture == "rock" and botInput == "scissors":
                    print('You win!')
                    rockPaperScissors("")
                   
                if chosenHandGesture == "paper" and botInput == "rock":
                    print('You win!')
                    rockPaperScissors("")
                  
    else:
        if chosenHandGesture == "I will never submit" or chosenHandGesture == "No":
            print('Yes, you are and will.')
            forcedrand = random.randint(1,3)
            finalValue = 0
            if forcedrand == 1:
                finalValue = "rock"
            if forcedrand == 2:
                finalValue = "paper"
            if forcedrand == 3:
                finalValue = "scissors"
            rockPaperScissors(finalValue)
        else:   
            print('The input you entered is numerical or invalid.')
            
            
            
rockPaperScissors("")
