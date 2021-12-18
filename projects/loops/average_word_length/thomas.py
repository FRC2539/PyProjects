#Thomas Zimmerman
punctuation = """!()-[]}{"';:\/,><./?@#$%^&*_~"""

def checkSentence(sentence):
    characternumber = 0
    wordnumber = 0
    splitablesentence = ""
    for character in sentence:
        if character not in punctuation:
            splitablesentence = splitablesentence + character
    splitSentence = splitablesentence.split()
    print(splitSentence)
    for v in splitSentence:
       wordnumber = wordnumber + 1
       splitword = list(v)
      
       for i in splitword:
           
            characternumber = characternumber + 1
           
    average = int(characternumber/wordnumber)
    print('The average word length should be something around: ', str(average))
print('Input something!')
checkSentence(input())
