def is_odd(n):
    return n%2 == 1

def has_odds(x):
    for n in x:
        if is_odd(n):
            return True
    return False

def all_odds(x):
    for n in x:
        if not is_odd(n):
            return False
    return True

def no_odds(x):
    return not has_odds(x)

def get_odds(x):
    l = []
    for n in x:
        if is_odd(n):
            l.append(n)
    return l

def zip_odds(a,b):
    a = get_odds(a)
    b = get_odds(b)
    l = []
    for k in range(min(len(a),len(b))):
        l.append(a[0])
        a.pop(0)
        l.append(b[0])
        b.pop(0)
    if len(a) <= len (b):
        return l + b
    return l + a
    
exec(input().strip())

#17 min