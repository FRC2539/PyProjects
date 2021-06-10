#Wyatt Petula
def tempConversionToC(inputTemp):
    fTemp = (inputTemp * 1.8) + 32
    print("F temperature: ", fTemp)
    
tempConversionToC(-40)

def tempConversionToF(inputTemp):
    cTemp = (inputTemp - 32) / 1.8
    print("C temperature: ", cTemp)
    
tempConversionToF(-40)
