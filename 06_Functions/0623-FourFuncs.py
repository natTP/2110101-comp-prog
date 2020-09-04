def make_int_list(x):
    return [ int(c) for c in x.split() ]

def is_odd(e):
    if e%2 == 1:
        return True
    else:
        return False

def odd_list(alist):
    l = []
    for k in alist:
        if is_odd(k):
            l.append(k)
    return l

def sum_square(alist):
    sqsum = 0
    for k in alist:
        sqsum += k**2
    return sqsum

exec(input().strip())