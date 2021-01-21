#!/usr/bin/env python3

'''        
Answer Key:
"tacocat" = palindrome
"RAcECaR" = palindrome
"cow" = not a palindrome
"litliceecilit" = not a palindrome

Code below (7 lines):
'''

running = True
while running:
    stringToTest = str(input('Please enter a string to check: '))
    if stringToTest.lower() == (stringToTest.lower())[::-1]: # .lower() makes everything lowercase!
        print(stringToTest + ' is a palindrome!')
    else:
        print(stringToTest + ' is NOT a palindrome.')
