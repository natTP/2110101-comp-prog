h = int(input())

w = 2*h - 1
for i in range(h-1):
    line = ""
    for space in range(h-1-i):
        line += " "
    line += "*"
    for space in range(2*i-1):
        line += " "
    if i != 0:
        line += "*"
    for space in range(h-1-i):
        line += " "
    print(line)
line = ""
for i in range(w):
    line += "*"
print(line)
