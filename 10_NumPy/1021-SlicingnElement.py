import numpy as np 

def sum_2_rows(M):
    even = M[::2,:]
    odd = M[1::2,:]
    return even + odd  

def sum_left_right(M):
    left = M[:,:M.shape[1]//2]
    right = M[:,M.shape[1]//2:]
    return left + right

def sum_upper_lower(M):
    upper = M[:M.shape[0]//2,:]
    lower = M[M.shape[1]//2:,:]
    return upper + lower

def sum_4_quadrants(M):
    q1 = M[:M.shape[0]//2,  M.shape[1]//2:]
    q2 = M[:M.shape[0]//2,  :M.shape[1]//2]
    q3 = M[M.shape[0]//2:,  :M.shape[1]//2]
    q4 = M[M.shape[0]//2:,  M.shape[1]//2:]
    return q1+q2+q3+q4
    #OR return sum_left_right(sum_upper_lower(M))

def sum_4_cells(M):
    one = M[::2,::2]
    two = M[::2,1::2]
    three = M[1::2,::2]
    four = M[1::2,1::2]
    return one+two+three+four

def count_leap_years(y):
    y -= 543
    return y[ (y%400 == 0) | ((y%4 == 0) & (y%100 != 0)) ].shape[0]

exec(input().strip())  