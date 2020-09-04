w = int(input())

if w<= 100:
    print(18)
elif w>100 and w<=250:
    print(22)
elif w>250 and w<=500:
    print(28)
elif w>500 and w<=1000:
    print(38)
elif w>1000 and w<=2000:
    print(58)
else:
    print("Reject")