def findTot(l):
    tot = 0
    for k in l:
        tot += k
    return tot

def first_fit(L, e):
    for lis in L:
        if e + findTot(lis) <= 100:
            lis.append(e)
            return L
    L.append([e])
    return L

def best_fit(L, e):
    minn = float('inf')
    best = len(L)
    for i in range(len(L)):
        diff = 100 - (e + findTot(L[i]))
        if diff >= 0 and diff < minn:
            minn = diff
            best = i
    if best != len(L):
        L[best].append(e)
    else:
        L.append([e])
    return L

def partition_FF(D):
    L = []
    for k in D:
        L = first_fit(L,k)
    return L

def partition_BF(D):
    L = []
    for k in D:
        L = best_fit(L,k)
    return L

exec(input().strip())