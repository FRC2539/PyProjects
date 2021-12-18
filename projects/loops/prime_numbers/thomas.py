#Thomas Zimmerman

def checkPrime():
    print('Insert Number')
    insertedvalue = input()
    insertedvalue = abs(int(insertedvalue))
 
    prime = True
    
    for number in range(int(insertedvalue)):
        if number > 1:
            if insertedvalue % number == 0:
                prime = False
        
        
    
    
    if prime == True:
        print('This number is prime!')
    else:
        print('This number is not prime.')
        

checkPrime()
