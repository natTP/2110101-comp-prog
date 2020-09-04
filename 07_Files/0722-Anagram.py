def stripPunct(s): #also sorts letters
    l = []
    for c in s:
        if c not in " .(),;:!?\'\"":
            l.append(c)  
    l.sort()
    return "".join(l)

inp1 = stripPunct(input().lower())
inp2 = stripPunct(input().lower())

if inp1 == inp2:
    print("YES")
else:
    print("NO")
