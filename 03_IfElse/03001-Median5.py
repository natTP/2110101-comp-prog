a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a>b:
    t = a
    a = b
    b = t
if c>d:
    t = c
    c = d 
    d = t
if a>c:
    t = b
    b = d 
    d = t
    c = a
a = e
if a>b:
    t = a
    a = b
    b = t
if c>a:
    t = b
    b = d 
    d = t
    a = c
if a>d:
    print(d)
else:
    print(a)