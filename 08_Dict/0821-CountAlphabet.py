s = input().lower()
cnt = {}
for c in s:
    if c in "abcdefghijklmnopqrstuvwxyz":
        if c not in cnt:
            cnt[c] = 1
        else:
            cnt[c] += 1
sortedcnt = [[-1*v,k] for k,v in cnt.items()]
sortedcnt.sort()
for k in sortedcnt:
    print(k[1],"->",-1*k[0])
