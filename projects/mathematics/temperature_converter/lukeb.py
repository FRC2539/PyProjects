print('Is your number celsius or fahrenheit?')
w = input()
w = w.lower()
print ('Enter your number')
if w == ('fahrenhet'):
    x = input()
    if not x.isnumeric():
        print ('Thats a word')
    else:
        x = int(x)
        if x < 0:
            print ('Error')
        else:
            y = x * 2
            z = y + 30
            print (z)
else:
    x = input()
    if not x.isnumeric():
        print ('Thats a word')
    else:
        x = int(x)
        if x < 0:
            print ('Error')
        else:
            y = x * 2
            z = y + 30
            print (z)
