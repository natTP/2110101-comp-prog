depts = {}

n = int(input())
for i in range(n):
    d,n = input().split()
    depts[d] = int(n)

m = int(input())
stu = []
for i in range(m):
    inp = input().split()
    stu.append( [ float(inp[1]), inp[0], inp[2:] ] )
stu.sort(reverse = True)

ans = []
for s in stu:
    for d in s[2]:
        if depts[d] > 0:
            ans.append([s[1],d])
            depts[d] -= 1
            break
ans.sort()

for a in ans:
    print(a[0],a[1])