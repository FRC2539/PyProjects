import random
print('Lets play rps, what do you pick?')
x = input()
x = x.lower()
print('I pick:')
mylist = ["rock", "paper", "scissor"]
z = random.choice(mylist)
print(z)
if x == 'rock' and z == 'rock':
    print('Tie!')
elif x == 'paper' and z == 'paper':
    print ('Tie!')
elif x == 'scissor' and z == 'scissor':
    print ('Tie!')
elif x == 'rock' and z == 'paper':
    print('You lose :(')
elif x == 'rock' and z == 'scissor':
    print('You win!')
elif x == 'paper' and z == 'rock':
    print('You win!')
elif x == 'paper' and z == 'scissor':
    print('You lose :(')
elif x == 'scissor' and z == 'rock':
    print('You lose:(')
elif x == 'scissor' and z == 'paper':
    print('You lose :(')
elif print('You dont know how to play do you...  Lets say you pick machine gun.  Well that wins everytime!'):
    pass
