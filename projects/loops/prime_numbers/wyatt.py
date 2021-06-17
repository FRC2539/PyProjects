#Wyatt Petula

def isPrime():
    print("Enter a number below")
    
    try:
        inputNumber = int(input())
        prime = True
    
        if inputNumber > 1:
            for number in range(2, inputNumber // 2):
                if (inputNumber % number == 0):
                    prime = False
        
            if prime == True:
                print("This number is prime")
            else:
                print("This number is not prime")
        else:
            print("This is not a prime number")
    except(ValueError):
        print("Is that a number? Is it?")

isPrime()
                
                
