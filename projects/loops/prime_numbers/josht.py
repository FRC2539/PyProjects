num = 47374637537372
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print("%s is not a prime number" % num)
            break
        else:
            print("%s is a prime number" % num)
            break
elif num < 0:
    print("invalid, is not positive.")
else:
    print("%s is not a prime number" % num)

