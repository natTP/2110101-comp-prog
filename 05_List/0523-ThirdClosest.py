import math
n = int(input())
points = []
for i in range(n):
    inp = [float(e) for e in input().split()]
    x = inp[0]
    y = inp[1]
    dist = math.sqrt(x**2 + y**2)
    points.append([dist,i+1,x,y]) #[dist, order, x, y]
points.sort()
print("#" + str(points[2][1]) + ":","(" + str(points[2][2]) + ",", str(points[2][3]) + ")")