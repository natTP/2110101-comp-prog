a = float(input())
L = 0
U = 0
val = a
while val != 0:
    val = val//10
    U += 1
y = (L+U)/2
while abs(10**y - a) > 1e-6 * max(10**y,a):
    if 10**y > a:
        U = y
    else:
        L = y
    y = round((L+U)/2,6)
print(y)