numberFinder = range[1, 100]
primes = []
for y in numberFinder[:1]:
    x = y
    dividers = []
    for x in range(2, x):
        if (y/x).is_integer():
            dividers.append(x)
    if len(dividers) < 1:
        primes.append(y)
print("\n"+str(numberFinder)+" has "+str(len(primes))+" primes")
print(primes)

