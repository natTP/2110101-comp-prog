import numpy as np 

def get_column_from_bottom_to_top( A, c ):
    return A[-1::-1,c]

def get_odd_rows( A ):
    return A[1::2]

def get_even_column_last_row( A ):
    return A[-1,::2]

def get_diagonal1( A ): # A is a square matrix  
    return np.array([ A[r,r] for r in range(A.shape[0]) ])

def get_diagonal2( A ): # A is a square matrix
    return np.array([ A[r,A.shape[0]-r-1] for r in range(A.shape[0]) ])

exec(input().strip())