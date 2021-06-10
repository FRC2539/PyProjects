prime = int(input("Enter value: "))

i = 2
if (prime < 0):
    print("invalid");
    quit()
while (i < prime):
    if (prime % i == 0):
        print("not prime")
        quit()
        
    else:
        i = i + 1
        
print("prime")
