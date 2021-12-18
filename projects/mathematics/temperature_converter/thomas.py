#Thomas Zimmerman
def temperatureConverter():
    print('fahrenheit or celsius?')
    selection = input().lower()
    change = input()
    if change.isnumeric():
        change = int(change)
        if selection == 'fahrenheit':
                cValue = (int(change) - 32) / 1.8
                print('The temperature in celsius is: ', str(cValue))
        else:
            if selection == 'celsius':
                fValue = (int(change) * 1.8) + 32
                print('The temperature in celsius is: ', str(fValue))
            else:
                print('This is not a selectable term. Check spelling, and re-enter')
    else:
      print("That's a word.")
temperatureConverter()
    
    
   
