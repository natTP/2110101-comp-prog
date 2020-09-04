validNames = ["Robert","Dick","William","Bill","James","Jim","John","Jack","Margaret","Peggy","Edward","Ed","Sarah","Sally","Andrew","Andy","Anthony","Tony","Deborah","Debbie"]
n = int(input())
for k in range(n):
    name = input()
    if name in validNames:
        i = validNames.index(name)
        if i%2 == 0: #realName
            print(validNames[i+1])
        else: #nickName
            print(validNames[i-1])
    else:
        print("Not found")

