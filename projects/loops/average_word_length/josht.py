mystring = "where can I get a glass of water? Do you not know?"

def averageWordLength(mystring):
    tempcount = 0
    count = 1
    
    wordcount = 0
    try:
        for character in mystring:
            if character == " ":
                tempcount += 1
                if tempcount == 1:
                    count += 1
                    
            else:
                tempcount = 0
                try:
                    if character.isalpha():
                        wordcount += 1
                except:
                        wordcount = wordcount + 0
                        
        if mystring[0] == " " or mystring.endswith(" "):
            count -= 1
            
        try:
            result = wordcount/count
            if result == 0:
                result = "no words"
                return result
            else:
                return result
        except ZeroDivisionError:
            error = "no words"
            return error 
    except Exception:
        error = "not a string"
        return error

print(averageWordLength(mystring))
