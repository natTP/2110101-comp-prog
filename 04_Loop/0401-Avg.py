d = []
inp = input()
while inp != "q":
    d.append(float(inp))
    inp = input()
n = len(d)
if n < 1:
    print("No Data")
else:
    i = 0
    tot = 0
    while i < n:
        tot += d[i]
        i += 1
    print(round(tot/n,2))