import numpy as np 

def mult_table(nrows,ncols):
    nr = np.arange(1,nrows+1).reshape(1,nrows).T
    nc = np.arange(1,ncols+1)
    return nr*nc

exec(input().strip())