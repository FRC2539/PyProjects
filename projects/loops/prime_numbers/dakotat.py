num = float(input('enter your number:'))
x = 2
factor = None

while x < num:
    if num % x == 0:
        print('Its not prime')
        factor = x
        break
    x += 1
    
if factor is not None:
    print(str(factor) + ' its prime')
