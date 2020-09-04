d = int(input())
m = int(input())
y = int(input())

y -= 543
if y%400 == 0 or (y%4 == 0 and y%100 != 0):
    leapY = True
else:
    leapY = False

daysinmo = [0,31,28,31,30,31,31,30,31,30,31,30,31]

totd = 0
for i in range(0,m):
    totd += daysinmo[i]
if leapY and m>2:
    totd += 1
totd += d

print(totd)