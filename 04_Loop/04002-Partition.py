d = [int(e) for e in input().split() ]

p = d[-1]
i = -1
j = 0
n = len(d)
while j < n-1:
    if d[j] <= p:
        i += 1
        temp = d[i]
        d[i] = d[j]
        d[j] = temp
    j += 1
temp = d[i+1]
d[i+1] = d[-1]
d[-1] = temp
print(d)