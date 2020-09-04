stations = {} #dict of set

inp = input().split()
while len(inp) == 2:
    if inp[0] not in stations:
        stations[inp[0]] = set()
    stations[inp[0]].add(inp[1])
    if inp[1] not in stations:
        stations[inp[1]] = set()
    stations[inp[1]].add(inp[0])
    inp = input().split()

q = inp[0]
ans = set()
ans.add(q)
if q in stations:
    for s in stations[q]:
        ans.add(s)
        for s2 in stations[s]:
            ans.add(s2)
for s in sorted(ans):
    print(s)