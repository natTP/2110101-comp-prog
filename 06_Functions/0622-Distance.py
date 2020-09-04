import math

def distance1(x1,y1,x2,y2):
    dx = abs(x1-x2)
    dy = abs(y1-y2)
    return math.sqrt(dx**2 + dy**2)

def distance2(p1,p2):
    dx = abs(p1[0]-p2[0])
    dy = abs(p1[1]-p2[1])
    return math.sqrt(dx**2 + dy**2)

def distance3(c1,c2):
    dist = distance1(c1[0],c1[1],c2[0],c2[1])
    if c1[2] + c2[2] >= dist: 
        return "(" + str(dist) + ", True)"
    return "(" + str(dist) + ", False)"

def perimeter(points):
    perim = 0
    for i in range(len(points)):
        perim += distance2(points[i],points[(i+1)%len(points)])
    return perim

exec(input().strip())