def convex_polygon_area(p):
    p = list(p)
    xy = 0
    yx = 0
    for i in range(len(p)-1):
        xy += p[i][0]*p[i+1][1]
        yx += p[i][1]*p[i+1][0]
    xy += p[-1][0]*p[0][1]
    yx += p[-1][1]*p[0][0]
    return abs(0.5*(xy-yx))

def format_string(s):
    s = s.lower()
    ans = ""
    for c in s:
        if c in "abcdefghijklmnopqrstuvwxyz":
            ans += c
    return ans

def is_heterogram(s):
    s = format_string(s)
    l = []
    for c in s:
        if c in l:
            return False
        l.append(c)
    return True

def replace_ignorecase(s,a,b):
    ans = list(s)
    s = s.lower()
    a = a.lower()
    i = s.find(a)
    k = len(b)-len(a)
    firstTime = True
    while i != -1:
        if firstTime:
            ans[i:i+len(a)] = b
            firstTime = False
        else:
            ans[i+k:i+len(a)+k] = b
        i = s.find(a,i+len(a))
    return "".join(ans)

def top3(votes):
    l = [[-1*v,n] for n,v in votes.items()]
    l.sort()
    ans = []
    for item in l:
        ans.append(item[1])
    return ans[:3]
        
for k in range(2):
    exec(input().strip())
    
#36 min with interruptions