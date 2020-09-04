stu = {}
ans = set()

n = int(input())
for i in range(n):
    name, group, batch, dep = input().split()
    stu[name] = (group,batch,dep)
    ans.add(name)

search = input().split()
sets = []
for q in search:
    s = set()
    for key,val in stu.items():
        if q in val:
            s.add(key)
    sets.append(s)

for s in sets:
    ans = s & ans
names = sorted(ans)
if len(names) == 0:
    print("Not Found")
else:
    for name in names:
        print(name," ".join(stu[name]))