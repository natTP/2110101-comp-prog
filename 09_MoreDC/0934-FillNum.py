def pattern1(nrows,ncols):
    n = 1
    table = []
    for i in range(nrows):
        row = []
        for j in range(ncols):
            row.append(n)
            n += 1
        table.append(row)
    return table

def pattern2(nrows,ncols):
    n = 1
    table = []
    for i in range(nrows):
        row = []
        m = n
        for j in range(ncols):
            row.append(m)
            m += nrows
        table.append(row)
        n += 1
    return table

def pattern3(N):
    n = 1
    z = 0
    table = []
    for i in range(N):
        row = []
        for j in range(z):
            row.append(0)
        for j in range(z,N):
            row.append(n)
            n += 1
        z += 1
        table.append(row)
    return table

def pattern4(N):
    n = m = 1
    z = 0
    table = []
    for i in range(N):
        row = []
        m += n-1
        p = m
        inc = n+1
        for j in range(z):
            row.append(0)
        for j in range(z,N):
            row.append(p)
            p += inc
            inc += 1
        z += 1
        table.append(row)
        n += 1
    return table

def pattern5(N):
    n = 1
    z = 0
    table = []
    for i in range(N):
        row = []
        m = n
        inc = N
        for j in range(z):
            row.append(0)
        for j in range(z,N):
            row.append(m)
            m += inc
            inc -= 1
        z += 1
        table.append(row)
        n += 1
    return table

def pattern6(N): #18,21
    n = 1
    z = 0
    table = []
    for i in range(N):
        row = []
        m = n
        inc1 = (N-n)*2
        inc2 = 2*n - 1
        for j in range(z):
            row.append(0)
        for j in range(z,N):
            row.append(m)
            if (j-z) % 2 == 0:  #inc is decreasing even
                m += inc1
                inc1 -= 4
            else:               #inc is increasing odd
                m += inc2
        z += 1
        table.append(row)
        n += 1
    return table

exec(input().strip())