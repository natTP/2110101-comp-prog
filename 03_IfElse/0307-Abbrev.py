n = int(input())

if n<1000:
    print(n)
elif n<1e6:
    if n<1e4:
        print(str(round(n/1000,1)) + "K")
    else:
        print(str(round(n/1000)) + "K")
elif n<1e9:
    if n<1e7:
        print(str(round(n/1e6,1)) + "M")
    else:
        print(str(round(n/1e6)) + "M")
else:
    if n<1e10:
        print(str(round(n/1e9,1)) + "B")
    else:
        print(str(round(n/1e9)) + "B")