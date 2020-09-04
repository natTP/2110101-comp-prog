n1 = input().split()
n2 = input().split()

month = ["January","February","March","April","May","June","July","August","September","October","November","December"]

if n1[3] > n2[3]:
    print(n2[0])
elif n1[3] < n2[3]:
    print(n1[0])
else:
    if month.index(n1[1]) > month.index(n2[1]):
        print(n2[0])
    elif month.index(n1[1]) < month.index(n2[1]):
        print(n1[0])
    else:
        if int(n1[2][:-1]) > int(n2[2][:-1]):
            print(n2[0])
        elif int(n1[2][:-1]) < int(n2[2][:-1]):
            print(n1[0])
        else:
            print(n1[0],n2[0])