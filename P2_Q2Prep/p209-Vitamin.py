fruit = []

n = int(input())
for k in range(n):
    inp = input().split()
    for i in range(1,len(inp)):
        inp[i] = float(inp[i])
    fruit.append(inp)
    
inp = input().split()
q = inp[0]
if len(inp) == 2:
    val = inp[1]

if q == "show":
    for k in fruit:
        print(" ".join( [str(c) for c in k] ))

elif q == "get":
    found = False
    for i in range(n):
        if fruit[i][0] == val:
            found = True
            print(" ".join( [str(c) for c in fruit[i]] ))
            break
    if not found:
        print(val,"not found")
        
elif q == "avg":
    val = int(val)
    tot = 0
    for i in range(n):
        tot += fruit[i][val]
    print(round(tot/n,4))
    
elif q == "max":
    val = int(val)
    fruitmax = ""
    vmax = -1
    for i in range(n):
        if fruit[i][val] > vmax:
            vmax = fruit[i][val]
            fruitmax = fruit[i][0]
        elif fruit[i][val] == vmax:
            fruitmax = min(fruitmax,fruit[i][0])
    print(fruitmax, vmax)
    
elif q == "sort":
    val = int(val)
    f = []
    for i in range(n):
        f.append([fruit[i][val],fruit[i][0]])
    f.sort()
    ans = ""
    for i in range(n):
        ans += f[i][1] + " "
    print(ans[:-1])

#31 min