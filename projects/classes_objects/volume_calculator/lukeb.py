import time
print('Please enter your length')
number1 = input()
number1 = int(number1)
if number1 >0:
    pass
else:
    print('Dude... thats a negative number.')
    time.sleep(2)
    exit(print('Bye!'))
print('Please enter your width')
number2 = input()
number2 = int(number2)
if number2 >0:
    pass
else:
    print('Dude... thats a negative number.')
    time.sleep(2)
    exit(print('Bye!'))
print('Please enter your height')
number3 = input()
number3 = int(number3)
if number3 >0:
    pass
else:
    print('Dude... thats a negative number.')
    time.sleep(2)
    exit(print('Bye!'))

class something:
    def __init__(self, number1, number2, number3):
        self.length = number1
        self.width = number2
        self.height = number3
        
        self.answer1 = self.length*self.width
        self.finalanswer = self.answer1*self.height
        n = something(number1,number2,number3,answer1,finalanswer)
        print('Ok answer is',self.finalanswer)
