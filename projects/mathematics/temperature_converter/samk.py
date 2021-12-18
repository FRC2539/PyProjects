def convert(inp):
    # Stop if input value is not a number.
    if type(inp) != int:
        return
    
    # Return value after converting to fahrenheit.
    return inp*(9/5)+32

print(convert("HI"))
