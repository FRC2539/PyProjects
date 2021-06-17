#Wyatt Petula--WIP
#Tested--yes
def primes(inputNumber):
    try:
        prime = True
        if inputNumber > 1:
            for number in range(1, inputNumber // 2):
                if (inputNumber % number == 0):
                    print("False--modable")
                    prime = False
        
            if prime == True:
                print("True")
                return True
            else:
                print("False")
                return False
        else:
            print("False--lessthan")
            return False
    except(ValueError):
        print("False--valtime")
        return False
    
#WIP
def mPrimeFinder(upperLimit):
    primeList = []
    for numbers in range(1, upperLimit + 1):
        if primes(numbers) - 1 == True:
            print("Yes")
            primeList.append(numbers)
    print(primeList)
        

mPrimeFinder(10)
print("\n\n")
