import math

a = float(input())
b = float(input())
c = float(input())

val = math.sqrt(b**2-4*a*c)

print(round((-b-val)/(2*a),3),round((-b+val)/(2*a),3))