#Wyatt Petula -- WIP

#Calculate the total volume.
def calcDimensions(dimensions):
    totals = []
    for index in range(0, len(dimensions) - 1):
        
    
    return totals

#Get the user's desired dimensions.
def inputDimensions():
    try:
        numOfRects = int(input("Enter the number of rectangles that you want to calculate the total volume of: "))
        dimensionList = []
        
        #Store all the desired inputs.
        for index in range(0, numOfRects):
            for indexTwo in range(0, 3):
                dimensionList.append(int(input("Enter a dimension of rectangle number " + str(index + 1) + ": ")))
            
        print(calcDimensions(dimensionList))

    except ValueError or ArithmeticError:
        print("Please input only positive numbers!")

inputDimensions()
        
        
    
