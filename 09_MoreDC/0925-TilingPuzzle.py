def row_number(t, e):
    for i in range(len(t)):
        if e in t[i]:
            return i
    return None
    
def flatten(t):
    ans = []
    for row in t:
        for e in row:
            if e != 0:
                ans.append(e)
    return ans
    
def inversions(x):
    cnt = 0
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i] > x[j]:
                cnt += 1
    return cnt
    
def solvable(t):
    if len(t)%2 == 1:
        if inversions(flatten(t))%2 == 0:
            return True
        return False
    if inversions(flatten(t))%2 == 1:
        if row_number(t,0)%2 == 0:
            return True
        return False
    if row_number(t,0)%2 == 1:
        return True
    return False
    
exec(input().strip())