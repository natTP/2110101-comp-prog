import numpy as np

def eq(A,B,p):
    n = 1
    for i in A.shape:
        n *= i
    per = np.sum(A==B)/n * 100
    return per >= p

def closest_point_indexes(points,p):
    dx = (points[::,:1] - p[0]) ** 2
    dy = (points[::,1:] - p[1]) ** 2
    dist = np.sqrt(dx + dy)        #actually not necessary!!
    i = np.arange(dist.shape[0])
    ans = dist == np.min(dist)
    return i[ ans.reshape(ans.shape[0]) ]

def number_of_inversions(A):
    i = np.arange(A.shape[0])
    iT = i.reshape((A.shape[0],1))
    AT = A.reshape((A.shape[0],1))
    return np.sum((AT > A) & (iT < i))
    #mat = np.triu(A.reshape((A.shape[0],1)) - A)
    #return np.sum(mat > 0) 
    
exec(input().strip())