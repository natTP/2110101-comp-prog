import math
bd, bm, by, d, m, y = [int(e) for e in input().split()]
daysinmo = [0,31,28,31,30,31,31,30,31,30,31,30,31]

t = (y-by-1)*365

#red zone
by -= 543
if by%400 == 0 or (by%4 == 0 and by%100 != 0):
    leapY = True
else:
    leapY = False
tred = daysinmo[bm]-bd
for i in range(bm+1,13):
    tred += daysinmo[i]
if leapY and bm <= 2:
    tred += 1

#blue zone
y -= 543
if y%400 == 0 or (y%4 == 0 and y%100 != 0):
    leapY = True
else:
    leapY = False
tblue = 0
for i in range(1,m):
    tblue += daysinmo[i]
if leapY and m>2:
    tblue += 1
tblue += d

t += tred + tblue

physical = math.sin((2*math.pi*t)/23)
emotional = math.sin((2*math.pi*t)/28)
intellectual = math.sin((2*math.pi*t)/33)
print(t,"{:.2f}".format(physical),"{:.2f}".format(emotional),"{:.2f}".format(intellectual) )