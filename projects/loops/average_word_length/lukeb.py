print('Enter a sentence.')
x = input()
if x == 'Mr':
    x = x.split()
    x = len(x)
    y = (x - 1)
    print(y)
else:
    print(x)
    x = x.split()
    x = len(x)
    print(x)
