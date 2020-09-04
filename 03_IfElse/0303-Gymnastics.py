a,b,c,d = [float(e) for e in input().split()]

tot = a+b+c+d
most = max(max(a,b),max(c,d))
least = min(min(a,b),min(c,d))

print(round((tot-most-least)/2,2))