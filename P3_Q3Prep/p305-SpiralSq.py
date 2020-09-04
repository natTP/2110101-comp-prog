def fill(A,r,c,direc,k):
    for i in range(k):
        A[r+direc[0]][c+direc[1]] = A[r][c] + 1
        r += direc[0]
        c += direc[1]
    return r,c
    
def spiral_square(n): # n is a positive odd number
    A = [ [0]*n for i in range(n) ]
    r = c = n//2
    A[r][c] = 1
    direc = [(0,1),(-1,0),(0,-1),(1,0)] #r,u,l,d
    d = 0
    for i in range(1,n):
        r,c = fill(A,r,c,direc[d],i)
        d = (d+1)%4
        r,c = fill(A,r,c,direc[d],i)
        d = (d+1)%4
    if n > 1:
        fill(A,r,c,direc[d],i)
    return A
    
def print_square(S):
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))

exec(input().strip())