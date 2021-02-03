print('Enter your word')
x = input()
x = x.lower()
y = x[::-1]
if y == x:
    print('True')
else:
    print('False')
