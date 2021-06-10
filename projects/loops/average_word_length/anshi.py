punctuation = """!()-[]}{"';:\/,><./?@#$%^&*_~"""
input_sentence = """We the People of the United States, in Order to form a more perfect Union, 
establish Justice, insure domestic Tranquility, provide for the common defence, 
promote the general Welfare, and secure the Blessings of Liberty to ourselves 
and our Posterity, do ordain and establish this Constitution for the United 
States of America."""

sentence = ""
for char in input_sentence:
   if char not in punctuation:
       sentence = sentence + char
       
wordQuantity = sentence.split()
avg = sum(len(wordLength) for wordLength in wordQuantity) / len(wordQuantity)
print(avg)





