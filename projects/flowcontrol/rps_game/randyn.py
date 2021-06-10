import random
e = input("Rock, paper, scissors! ")

opponent = random.randint(1, 3)
if (opponent == 1):
    x = "rock"
elif (opponent == 2):
    x = "paper"
else:
    x = "scissors"
print("Commputer: " + x)

i = len(e)
if (i == 4):
    selection = 1
elif (i == 5):
    selection = 2
else:
    selection = 3
    
if (selection == opponent):
    print("Draw!")
elif (selection == 1 and opponent == 2):
    print("You lose")
elif (selection == 1 and opponent == 3):
    print("You win")
elif (selection == 2 and opponent == 1):
    print("You win")
elif (selection == 2 and opponent == 3):
    print("You lose")
elif (selection == 3 and opponent == 1):
    print("You lose")
else:
    print("You win")
