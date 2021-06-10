while True:
    try:
        temp = float(input("enter your temperature:"))
        c = (temp * 9/5) + 32
        print(c)
    except:
        continue
