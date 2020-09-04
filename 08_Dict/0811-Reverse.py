def reverse(d):
    rd = {}
    for key in d:
        rd[d[key]] = key
    return rd

def keys(d,v):
    the_keys = []
    for key in d:
        if d[key] == v:
            the_keys.append(key)
    return the_keys

exec(input().strip())