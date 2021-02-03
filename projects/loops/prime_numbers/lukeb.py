print('Enter your number')
x = input()
x = abs(int(x))

for num in range(x):
    if num == 1 or num == 0:
        continue
    else:
        if x % num == 0:
            print('not prime')
            break
