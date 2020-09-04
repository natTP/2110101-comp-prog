e1 = input()
e2 = ""
n = len(e1)
for i in range(n):
    if e1[i] == '(':
        e2 += '['
    elif e1[i] == '[':
        e2 += '('
    elif e1[i] == ')':
        e2 += ']'
    elif e1[i] == ']':
        e2 += ')'
    else:
        e2 += e1[i]
print(e2)