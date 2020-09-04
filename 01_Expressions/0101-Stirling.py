import math

n = int(input())
a = math.sqrt(2*math.pi)
b = n**(n+0.5)
c = math.e**(-n+1/(12*n))
d = math.e**(-n+1/(12*n+1))
print(a*b*d)
print(a*b*c)
