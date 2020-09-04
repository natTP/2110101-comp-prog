def clear(s):
    ans = ""
    s = s.lower()
    for c in s:
        if c in "abcdefghijklmnopqrstuvwxyz":
            ans += c
    return ans

A = {}
B = {}
deleteA = []
deleteB = []

inp_a = input()
inp_b = input()
a = clear(inp_a)
b = clear(inp_b)
for c in a:
    if c not in A:
        A[c] = 1
    else:
        A[c] += 1
for c in b:
    if c not in B:
        B[c] = 1
    else:
        B[c] += 1

for c in A:
    if c in B:
        #if A[c] == B[c] #is the anagram
        if A[c] > B[c]:
            deleteA.append([c,A[c]-B[c]])
        elif A[c] < B[c]:
            deleteB.append([c,B[c]-A[c]])
    else:
        deleteA.append([c,A[c]])
for c in B:
    if c not in A:
        deleteB.append([c,B[c]])

deleteA.sort()
deleteB.sort()

print(inp_a)
if len(deleteA) == 0:
    print(" - None")
else:
    for k in deleteA:
        if k[1] == 1:
            print(" - remove",k[1],k[0])
        else:
            print(" - remove",k[1],str(k[0]) + "'s")
print(inp_b)
if len(deleteB) == 0:
    print(" - None")
else:
    for k in deleteB:
        if k[1] == 1:
            print(" - remove",k[1],k[0])
        else:
            print(" - remove",k[1],str(k[0]) + "'s")
            
#20 min, forgot to sort